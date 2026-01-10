#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "usage: adder <a> <b>\n";
        return 1;
    }

    int a = std::atoi(argv[1]);
    int b = std::atoi(argv[2]);

    std::cout << (a + b) << "\n";
    return 0;
}
