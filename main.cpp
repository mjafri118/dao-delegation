#define num_agents 10
#define num_limits 5
#define trials_per_limit 1000

#include <iostream>

int main(void) {
  int limit_list[num_limits];
  for (int i = 0; i < num_limits; ++i) {
    limit_list[i] = i * num_agents / num_limits + 1;
  }
  std::cout << limit_list << std::endl;
}