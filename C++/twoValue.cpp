#include <string>
#include <vector>

using namespace std;

long long solution(int a, int b) {
	long long answer = 0;

	if (a == b) {
		answer = a;
	}
	else {
		if (a > b) {
			int c = a;
			a = b;
			b = c;
		}
		for (a; a <= b; a++) {
			answer += a;
		}
	}
	return answer;
}