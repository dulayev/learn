#include "ChronoTest.h"

//TODO: move this to separate file
#include <iostream>
using namespace std;

class Grand {
public:
	virtual void Report()  { cout << "Grand"; }
};

class Parent : public Grand {
public:
	 // no matter has virtual or not
	void Report() override { cout << "Parent"; }	
};

class Child : public Parent {
public:
	virtual void Report() override { cout << "Child"; }
};

int main() {

	Child child;
	
	Grand* grand = &child;
	
	grand->Report();
	
	Parent* parent = &child;
	
	parent->Report();

    ChronoTest();

    return 0;
}
