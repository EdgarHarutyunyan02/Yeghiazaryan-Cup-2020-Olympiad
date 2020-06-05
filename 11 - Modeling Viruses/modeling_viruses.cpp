#include <iostream>
#include <math.h>

using namespace std;

int main() {
	double time = 0;
	double dt = 0.00001;
	int max_t;
	cin >> max_t;
	int a_x, a_y, a_v_x, a_v_y, b_x, b_y, b_v_x, b_v_y;

	cin >> a_x >> a_y >> a_v_x >> a_v_y;
	cin >> b_x >> b_y >> b_v_x >> b_v_y;

	while (time <= max_t) {
		double alice_pos_x = a_x + a_v_x * time;
		double alice_pos_y = a_y + a_v_y * time;

		double bob_pos_x = b_x + b_v_x * time;
		double bob_pos_y = b_y + b_v_y * time;

		double distance = sqrt(pow((alice_pos_x - bob_pos_x), 2) + pow((alice_pos_y - bob_pos_y), 2));
		if (distance <= 2) {
			cout << time << endl;
			return 0;
		}
		time += dt;
	}

	cout << -1 << endl;
	return 0;
}