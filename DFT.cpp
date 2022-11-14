/*
-------- DFT Project
-------- Bardia Yaghmaie - 400442396
-------- Data Structure
*/
#include <bits/stdc++.h>
using namespace std;


class Complex{ 
    
    public:
        double a, b; 
        


    Complex(double _a,double _b){
        this->a = _a;
        this->b = _b;
    }

    Complex(){}

    double get_a(){return a;}
    double get_b(){return b;}


    Complex operator * (Complex c2){
        double oa = (a * c2.a) - (b * c2.b);
        double ob = (a * c2.b) + (b * c2.a);
        Complex output(oa,ob);
        return output;
    }
    Complex operator + (Complex c2){
        double oa = a+c2.a;
        double ob = b+c2.b;
        Complex output(oa,ob);
        return output;
    }

    Complex powX(int n){
        Complex output(1,0);
        Complex c(this->a , this->b);
        for(int i=0; i<n; i++){
            output = output * c;
        }
        return output;
    
    }

};

Complex w(int n){ 
    double taghrib = 0.000001; 
    if(n==0){
        Complex c(1,0);
        return c;
    }
    else{
    double x = M_PI*0.5*n;
    double sine,cosine;
    if (abs(cos(x))<taghrib)
        cosine = 0;
    else 
        cosine = cos(x);
    if (abs(sin(x))<taghrib) 
        sine = 0;
    else 
        sine = sin(x);
    
    return Complex(cosine , -sine);;
    }
    
}

int main(){
    cout<<"Enter n:"<<endl;
    int n;
    cin>>n;
    Complex a[n];
    Complex b[n];

    for(int i=0;i<n;i++){
        double rp,ip;
        cout<<"Enter a"<<i<<" real: "<<endl;
        cin>>rp;
        cout<<"Enter a"<<i<<" imag: "<<endl;
        cin>>ip;
        Complex c(rp,ip);
        a[i] = c;
    }

    for(int i=0;i<n;i++){
        Complex bi(0,0);
        for (int j=0;j<n;j++) {
           bi = bi + (w(i).powX(j) * a[j]);
        }
        b[i] = bi;
    }
    cout<<endl<<endl;
    for(int i=0;i<n;i++){
        if(b[i].get_b()>=0) cout<<"b"<<i<<"== "<<b[i].get_a()<<" +"<<b[i].get_b()<<"i"<<endl;
        else cout<<"b"<<i<<"== "<<b[i].get_a()<<" "<<b[i].get_b()<<"i"<<endl;
        
    }
}