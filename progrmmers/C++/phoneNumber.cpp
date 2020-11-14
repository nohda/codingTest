#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<unordered_map>

using namespace std;

bool compare(const string &s1, const string &s2) {
	if (s1.size() == s2.size()) {
		return s1 < s2; //����� ������, ������ ������
	}
	return s1.size() < s2.size(); // ������ �ٸ��� ������ ������
}
bool solution(vector<string> phone_book) {
	// � ��ȣ�� �ٸ���ȣ�� ���ξ��� ��찡 ������ false,�ƴϸ� true
	bool answer = true;
	sort(phone_book.begin(), phone_book.end(), compare);
	unordered_map<string, int> map;
	vector<int> cnts;
	for (int i = 0; i < phone_book.size(); i++)
	{
		int length = phone_book[i].size();
		for (int j = 0; j < cnts.size(); j++) {
			string str = phone_book[i].substr(0, cnts[j]);
			if (map.find(str) != map.end()) {
				answer = false;
				break;
			}
		}
		if (answer == false) {
			break;
		}
		if (cnts.size() == 0 || length != cnts[cnts.size() - 1]) {
			cnts.push_back(length);
		}
		map.insert(make_pair(phone_book[i], i));
	}
	return answer;
}