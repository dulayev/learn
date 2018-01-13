#ifndef CHRONO_H
#define CHRONO_H

#include <chrono>
#include <iostream>

#define PRINT(msg, var) std::cout << msg << ": " << var << ";" << std::endl;

template<typename Timer>
void TestTimer(const char* name)
{
    using namespace std::chrono;
    
    PRINT("Timer", name);
    
    typename Timer::time_point tp = Timer::now();
    PRINT("Now from epoch", tp.time_since_epoch().count());
    typename Timer::time_point start = Timer::now();
    typename Timer::duration dur {}; // without {} is not inited by default
    PRINT("system_clock::duration init", dur.count());
    
    while(dur.count() == 0) {
        dur = Timer::now() - start;
    }
    PRINT("system_clock::duration min adjustment", dur.count());
    
    duration<double, seconds::period> d3 = dur;
    PRINT("system_clock::duration min adjustment (seconds)", d3.count());
};

inline void ChronoTest()
{
    using namespace std::chrono;
    
    std::chrono::duration<int> d1 = std::chrono::seconds(50);
    PRINT("50 seconds", d1.count());
    
    std::chrono::duration<float, std::chrono::minutes::period> d2 = 
        std::chrono::duration_cast<decltype(d2)>(d1); // ok with precision loss

    PRINT("50 seconds in minutes", d2.count());
    
    d2 -= std::chrono::seconds(10); // compiled only if no precision loss
        
    PRINT("40 seconds in minutes", d2.count());

    TestTimer<system_clock>("system_clock");
    TestTimer<steady_clock>("steady_clock");
    TestTimer<high_resolution_clock>("high_resolution_clock");
}

#endif /* CHRONO_H */

