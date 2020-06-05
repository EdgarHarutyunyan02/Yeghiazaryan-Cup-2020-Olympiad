#include <iostream>

int main()
{
	int n, k;
	std::cin >> n >> k;
	int* d = new int[n];
	int* N = new int[n];

	for (int i = 0; i < n; i++) {
		std::cin >> d[i];
	}
	for (int i = 0; i < n; i++) {
		int max = d[i];
		for (int j = i-1; i-j < k && j >= 0; j--) {
			if (d[j] > max)
				max = d[j];
		}
		N[i] = max;
	}

	for (int i = 0; i < n; i++) {
		std::cout << N[i]<<' ';
	}
	std::cout << std::endl;

    delete[] d;
    delete[] N;
	return 0;
}