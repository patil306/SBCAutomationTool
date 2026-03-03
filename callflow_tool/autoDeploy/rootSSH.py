import logging
import paramiko
import os

class SSH:
    def __init__(self):
        pass

    def get_ssh_connection(self, ssh_machine, ssh_username, ssh_password):
        """Establishes a ssh connection to execute command.
          :param ssh_machine: IP of the machine to which SSH connection to be established.
          :param ssh_username: User Name of the machine to which SSH connection to be established..
          :param ssh_password: Password of the machine to which SSH connection to be established..
          returns connection Object
          """
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=ssh_machine, username=ssh_username, password=ssh_password, timeout=30)
        return client


    def run_sudo_command(self, ssh_username="root", ssh_password="abc123", ssh_machine="localhost", command="ls",
                         jobid="None"):
        """Executes a command over a established SSH connectio.
        :param ssh_machine: IP of the machine to which SSH connection to be established.
        :param ssh_username: User Name of the machine to which SSH connection to be established..
        :param ssh_password: Password of the machine to which SSH connection to be established..
        returns status of the command executed and Output of the command.
        """
        print(ssh_machine)
        print(ssh_username)
        print(ssh_password)
        conn = self.get_ssh_connection(ssh_machine=ssh_machine, ssh_username=ssh_username, ssh_password=ssh_password)
        command = "sudo -S -p '' %s" % command
        logging.info("Job[%s]: Executing: %s" % (jobid, command))
        stdin, stdout, stderr = conn.exec_command(command=command)
        stdin.write(ssh_password + "\n")
        stdin.flush()
        stdoutput = [line for line in stdout]
        stderroutput = [line for line in stderr]
        for output in stdoutput:
            logging.info("Job[%s]: %s" % (jobid, output.strip()))
        # Check exit code.
        logging.debug("Job[%s]:stdout: %s" % (jobid, stdoutput))
        logging.debug("Job[%s]:stderror: %s" % (jobid, stderroutput))
        logging.info("Job[%s]:Command status: %s" % (jobid, stdout.channel.recv_exit_status()))
        if not stdout.channel.recv_exit_status():
            logging.info("Job[%s]: Command executed." % jobid)
            conn.close()
            if not stdoutput:
                stdoutput = True
            return True, stdoutput
        else:
            logging.error("Job[%s]: Command failed." % jobid)
            for output in stderroutput:
                logging.error("Job[%s]: %s" % (jobid, output))
            conn.close()
            return False, stderroutput

    def putAll(self, localpath, remotepath, ssh_machine, ssh_username, ssh_password):
        ssh = self.get_ssh_connection(ssh_machine=ssh_machine, ssh_username=ssh_username, ssh_password=ssh_password)
        sftp = ssh.open_sftp()

        # Create remote directory if it doesn't exist
        try:
            sftp.stat(remotepath)
        except FileNotFoundError:
            sftp.mkdir(remotepath)

        if os.path.isfile(localpath):
            # Obtain file name from local path & append to remote path
            path = os.path.split(localpath)  # Returns a tuple (directory, filename)
            remote_filename = os.path.join(remotepath, path[1])
            print('  Copying %s' % remote_filename)
            sftp.put(localpath, remote_filename)

        elif os.path.isdir(localpath):
            if localpath.endswith('/'):
                for dirpath, dirnames, filenames in os.walk(localpath):
                    # Change local dirpath to match remote path. Ex: local/dir/.. to remote/dir/...
                    remotedir = dirpath.split('/')  # remotedir = [local, dir1, dir2, ...]
                    remotedir[0] = remotepath.rstrip('/')  # remotedir = [/remote, dir1, dir2, ...]
                    remotedir = '/'.join(remotedir)

                    # Traverse into each child directory and create sub directory if it doesn't exist on remote host
                    if dirnames:
                        for dirname in dirnames:
                            subdir = os.path.join(remotedir, dirname)

                            try:
                                sftp.stat(subdir)
                            except FileNotFoundError:
                                sftp.mkdir(subdir)

                    for filename in filenames:
                        localdir = os.path.join(dirpath, filename)
                        remotefile = os.path.join(remotedir, filename)
                        print('  Copying %s' % localdir)
                        sftp.put(localdir, remotefile)
            else:
                # Create path /remote/local/dir1...
                p = os.path.join(remotepath, localpath)

                try:
                    sftp.stat(p)
                except FileNotFoundError:
                    sftp.mkdir(p)

                for dirpath, dirnames, filenames in os.walk(localpath):
                    if dirnames:
                        for dirname in dirnames:
                            subdir = os.path.join(dirpath, dirname)
                            remotedir = os.path.join(remotepath, subdir)

                            try:
                                sftp.stat(remotedir)
                            except FileNotFoundError:
                                sftp.mkdir(remotedir)

                    for filename in filenames:
                        local_filename = os.path.join(dirpath, filename)
                        remote_filename = os.path.join(remotepath, local_filename)
                        print(' Copying %s' % local_filename)
                        sftp.put(local_filename, remote_filename)
        else:
            print('File or directory not found.')
