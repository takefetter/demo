#include <iostream>  
#include <iomanip>  
#include <string>  
#include <vector>  
#include <list>  
#include <cstdlib>  
using namespace std;  
class Process//使用一个类的对象表示一个进程  
{  
public:  
    string ID;//进程名  
    vector<int> UsedResource;//已用各资源数  
    vector<int> NeedResource;//对应的所需资源数  
    Process&operator=(const Process &p) //运算符重载用于赋值  
    {  
        if (this != &p)  
        {  
            this->ID = p.ID;  
            this->UsedResource = p.UsedResource;  
            this->NeedResource = p.NeedResource;  
        }  
          
        return *this;  
    }  
};   
int ProcessCount;//进程数  
int ResourceCount;//资源数  
vector<int>Available;//可用资源数  
vector<int>calc;//用于计算的资源vector  
list<Process> n;//进程的链表  
list<Process> Copy;//对于进程链表的拷贝  
list<Process> Copy_2;//对于进程链表的拷贝  
list<int>UsedResourceBuffer;  
list<int>NeedResourceBuffer;  
list<string> Safeyqueue;//安全序列  
bool ShowQueue ()//显示安全序列  
{  
    int a = 0;  
    if (Safeyqueue.size()!= 0) {  
        for (auto i=Safeyqueue.begin();i!=Safeyqueue.end();++i)//使用auto定义迭代器,设置循环  
        {  
            cout << *i;  
            if (a != (Safeyqueue.size ()-1)) {  
                cout << "->";  
                a++;  
            }  
        }  
        return true;  
    }  
    else return false;  
}  
bool safetyCheak () {//安全性算法  
    Safeyqueue.clear ();//清空Safeyqueue  
    Copy_2.clear ();//清空Copy_2  
    Copy_2 = Copy;  
    int cheaknumber1=1;  
    for (int i = ProcessCount; i > 0; i--)  
    {  
        cheaknumber1 =cheaknumber1+i;  
    }  
    int cheaknumber2 = 0;  
    while (1)  
    {  
        int tip = 0;  
        for (int b = 0; b < ResourceCount; b++)  
        {  
            if (Copy_2.front ().NeedResource[b] <= calc[b])  
            {  
                tip++;//单个资源符合要求标识符tip+1  
            }  
        }  
        if (tip == ResourceCount)//进程的所有资源均符合要求  
        {  
            for (int d = 0; d < ResourceCount; d++)  
            {  
                calc[d] = calc[d] + Copy_2.front ().UsedResource[d];  
            }  
            cheaknumber2 = 0;  
            Safeyqueue.push_back (Copy_2.front ().ID);  
            Copy_2.pop_front ();  
        }  
        if (cheaknumber2 >= ProcessCount) break;//在第一次循环中就找不到符合条件的进程，跳出循环  
        else if (cheaknumber1 == 0) break;//循环数大于最大可能的循环数，跳出循环  
        else if (Copy_2.size () == 0) return true;  
          
        Copy_2.push_back (Copy_2.front ());  
        Copy_2.pop_front ();  
        cheaknumber2++;  
        cheaknumber1--;  
    }  
    return false;  
}  
Process SetProcess (string ID)//为进程初始化所用的函数 返回进程  
{  
    Process Buffer;//创建Process对象  
    Buffer.ID = ID;//初始化ID  
    while (UsedResourceBuffer.size() != 0)//若UsedResourceBuffer不为空  
    {  
        Buffer.UsedResource.push_back (UsedResourceBuffer.front ());//将UsedResourceBuffer的头节点插入到对象UsdResource的尾部  
        UsedResourceBuffer.pop_front ();//删除UsedResourceBuffer的头节点  
    }  
    while (NeedResourceBuffer.size () != 0)//方法与上相同  
    {  
        Buffer.NeedResource.push_back (NeedResourceBuffer.front ());  
        NeedResourceBuffer.pop_front ();  
    }  
    return Buffer;//返回对象  
}  
void ShowAllProcess ()//显示全部进程及资源表  
{  
    if (n.size () == 0) {  
        cout << "无进程，请分配进程！" << endl;//n中无Process的对象  
        return;  
    }  
    cout << std::left << setw (4) << "ID\t"<<std::right<< setw (12) << "USED\t\t" <<std::right<< setw (12) << " NEED\t" << endl<<std::left << setw (4) << "资源";  
    for (int i = 1; i <= ResourceCount; i++)  
    {  
        cout <<"\t" << std::left << i;  
    }  
    for (int i = 1; i <= ResourceCount; i++)  
    {  
        cout  <<"\t" << std::left << i ;  
    }  
    for (auto a = n.begin(); a != n.end (); ++a)//定义迭代器设置循环  
    {  
        cout <<endl<<std::left <<setw (4) << a->ID<<"|\t";  
        for (unsigned int b = 0;b<(a->UsedResource.size());b++)  
        {if(b!= (a->UsedResource.size ()-1))  
            cout << setw (4) << a->UsedResource[b]<<"\t";  
        else cout << setw (4) << a->UsedResource[b] << "|\t";  
        }  
        for (unsigned int b = 0; b<(a->NeedResource.size ()); b++)  
        {  
            cout << setw (4) << a->NeedResource[b] << "\t";  
        }  
    }  
}  
int main ()  
{  
    while (1)  
    {  
        system ("cls");  
        system ("color F0");  
        int choose;  
        cout << "请输入需要进行的算法或需要进行的操作\n"  
            "1.设置进程个数\n""2.设置资源个数\n""3.为每个进程分配资源\n""4.设置空闲资源并自动检测是否合法\n""5.执行银行家算法(请求新的资源)\n""6.查看当前所有信息\n""7.清除所有内容\n""8.退出程序\n";  
        cout << "请输入您的选择:";  
        cin >> choose;  
        system ("cls");  
        if (choose == 1)  
        {  
            if (ProcessCount != 0) {  
                cout << "您已输入资源个数，个数为" << ProcessCount << endl;  
                cout << "若需更改必须清除全部数据" << endl;  
                system ("pause");  
                continue;  
            }  
            cout << "请输入进程个数(输入错误将会保持为零):";  
            cin >> ProcessCount;  
            if (ProcessCount <= 0) {  
                cout << "输入进程数目错误，请重试."<<endl;  
                ProcessCount = 0;  
                system ("pause");  
                continue;  
            }  
            cout << "输入进程个数成功！"<<endl;  
            system ("pause");  
        }  
        if (choose == 2)  
        {  
            if (ResourceCount != 0) {  
                cout << "您已输入资源个数，个数为" << ResourceCount << endl;  
                cout << "若需更改必须清除全部数据" << endl;  
                system ("pause");  
                continue;  
            }  
            cout << "请输入资源个数(输入错误将会保持为零):";  
            cin >> ResourceCount;  
            if (ResourceCount <= 0) {  
                cout << "输入资源个数错误，请重试."<<endl;  
                ResourceCount = 0;  
                system ("pause");  
                continue;  
            }  
            cout << "输入资源个数成功！" << endl;  
            system ("pause");  
        }  
        if (choose == 3)  
        {  
            if ((ProcessCount == 0) || (ResourceCount == 0)) {  
                cout << "请先分配资源和进程再重试！" << endl;  
                system ("pause");  
                continue;  
            }  
            for (int i = 0; i < ProcessCount; i++)  
            {  
                cout << "请输入第"<<i+1<<"个进程的ID:";  
                string ID;  
                cin >> ID;  
                for (int i1 = 1; i1 <= ResourceCount; i1++)  
                {  
                    int a,b;  
                    cout << "请输入第" << i+1 << "个进程的第" << i1 << "个资源的占用数目:";  
                    while ((cin >> a) && (a < 0))  
                    {  
                        cout << endl<<"输入不符合规则，请重试:";  
                    }  
                    cout << "请输入第" << i + 1 << "个进程的第" << i1 << "个资源的需求数目:";  
                    while ((cin >> b) && (b< 0))  
                    {  
                        cout << endl << "输入不符合规则，请重试:";  
                    }  
                    UsedResourceBuffer.push_back (a);  
                    NeedResourceBuffer.push_back (b);  
                }  
                n.push_back(SetProcess (ID));  
            }  
            cout << endl << "当前所有程序状态如下\n";  
            ShowAllProcess ();  
            system ("pause");  
          }  
        if (choose == 4) {  
            if ((ProcessCount == 0) || (ResourceCount == 0)) {  
                cout << "请先分配资源和进程再重试！" << endl;  
                system ("pause");  
                continue;  
            }  
            Available.clear ();  
            for (int i = 0; i < ResourceCount; i++)  
            {  
                int a;  
                cout << "请设置第" << i + 1 << "个资源的空闲个数:";  
                while ((cin >> a) && (a < 0))  
                {  
                    cout <<endl<< "输入数值不合法,请重试:";  
                }  
                Available.push_back (a);  
            }  
            calc.clear ();  
            calc = Available;  
            Copy.clear ();  
            Copy = n;  
            bool b=safetyCheak ();  
            if (b == true) {  
                cout << "当前情况安全!"<<endl;  
                cout << "可执行的序列有(可能不唯一,这里只显示一种):";  
                ShowQueue ();  
                system ("pause");  
                continue;  
            }  
            if (b == false) {  
                cout << "当前情况不安全无法按当前值设置空闲资源!"<<endl;  
                cout << "请更改后重试!";  
                Available.clear ();  
                system ("pause");  
                continue;  
            }  
        }  
        if (choose == 5) {  
            if ((ProcessCount == 0) || (ResourceCount == 0)) {  
                cout << "请先分配资源和进程再重试！" << endl;  
                system ("pause");  
                continue;  
            }  
            vector<int>buffer;//存储当前进程请求的资源  
            buffer.clear ();  
            calc.clear ();  
            calc=Available;  
            Copy.clear ();  
            Copy = n;  
            string id;  
            //显示所有进程状态  
            cout << "当前资源情况如下:" << endl;  
            ShowAllProcess ();  
            cout << endl<<"当前资源状态如下" << endl;  
            for (auto i = Available.begin(); i != Available.end (); ++i)  
            {  
                cout << *i << "\t";  
            }  
            cout << endl << "请输入需要资源的进程名:";  
            cin >> id;  
            //对进程进行查找  
            for (auto a = Copy.begin (); a != Copy.end (); ++a) {  
                if (id == a->ID) {  
                    cout << endl << "找到此进程!";  
                    cout << "请输入目前是否需要分配资源,输入-1取消分配其他数字继续:";  
                    int c; cin >> c;  
                    if (c == -1) {  
                        cout << "取消分配!"; system ("pause"); continue;  
                    }  
                    cout << "请输入" << id << "进程" << "需要的资源个数:" << endl;  
                    //输入当前需要资源个数  
                    for (int d = 0; d < ResourceCount; d++)  
                    {  
                        int e;  
                        cout << "请输入第" << d+ 1 << "个资源个数:";  
                        while ((cin >> e) &&( (e <0)||(e>a->NeedResource[d])||(e>calc[d]))){  
                            if (e < 0)   cout << "输入不符合规则";  
                            if (e > a->NeedResource[d]) cout << "输入的数大于需要的资源数";  
                            if (e > calc[d]) cout << "输入的数大于系统的资源数";  
                            cout<<",输入错误,请重试:" << endl;  
                        }  
                        a->UsedResource[d] = a->UsedResource[d] + e;  
                        a->NeedResource[d] = a->NeedResource[d] - e;  
                        calc[d] = calc[d] - e;  
                        buffer.push_back (e);  
                    }  
                    bool boolean = safetyCheak ();//执行安全性算法检测  
                    if (boolean == true) {  
                        int f;  
                        cout << "当前情况安全！" << endl;  
                        cout << "是否要将资源赋给" << id << "?0确定,其他取消\n请输入你的选择:";  
                        cin >> f;  
                        if (f == 0) {//确定分配  
                            n.clear ();  
                            n = Copy;  
                            vector<int>buffer1;  
                            buffer1 = Available;  
                            Available.clear ();  
                            for (int b = 0; b < ResourceCount; b++)  
                            {  
                                buffer1[b]=buffer1[b] - buffer[b];  
                            }  
                            Available = buffer1;  
                            cout << "本次已成功赋予资源！"<<endl;  
                        }  
                        else {  
                            cout << "已取消！"<<endl;  
                        }  
                      
                    }  
                    if(boolean==false){  
                        cout << "不安全！因此无法分配！"<<endl;  
                    }  
                    cout <<endl<< "当前进程资源情况如下：\n";  
                    ShowAllProcess ();  
                    cout << endl<< "可用资源个数按顺序分别为:";  
                    for (auto i = Available.begin (); i != Available.end (); ++i)  
                    {  
                        cout << *i << "  ";  
                    }  
                    cout <<endl <<"可执行的队列如下\n";  
                    ShowQueue ();  
                    system ("pause");  
                    continue;  
                }  
            }  
        }  
        if (choose == 6) {  
            cout << "进程个数为" << ProcessCount << endl;  
            cout << "资源个数为" << ResourceCount << endl;  
            cout << "可用资源个数按顺序分别为:";  
            for (auto i = Available.begin (); i != Available.end(); ++i)  
            {  
                cout << *i<<"  ";  
            }  
            cout << "当前所有程序状态如下\n";  
            ShowAllProcess ();  
            cout << endl;  
            bool b=ShowQueue ();  
            if(b==false)cout<<"没有合适的可执行队列，请分配正确的资源！"<<endl;  
            system ("pause");  
        }  
        if (choose == 7) {  
            int a;  
            cout << "确认全部删除么?删除请输入0"<<endl;  
            cout << "请输入:";  
            cin >> a;  
            if (a != 0) continue;  
            ProcessCount=0;  
            ResourceCount=0;  
            Available.clear();  
            n.clear();  
            UsedResourceBuffer.clear();  
            Safeyqueue.empty();  
            cout << "全部删除成功！";  
            system ("pause");  
        }  
        if (choose == 8) {  
            cout << "退出程序！\n";  
            system ("pause");  
            exit (0);  
        }  
        }  
        return 0;  
    }  