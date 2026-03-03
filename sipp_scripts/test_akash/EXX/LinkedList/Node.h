template <class T>
class Node
{
 T data;
 Node *next;
public:
 Node();
 void setData(T data);
 T getData();
 void setNext(Node *temp);
 Node* getNext();
};
