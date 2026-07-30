class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string = "";

        for (string str : strs) {
            encoded_string = encoded_string + to_string(str.size()) + "83928" + str;
        }

        return encoded_string;
    }

    vector<string> decode(string s) {
        vector<string> decoded_strings;
        cout << s;
        while (s.size() > 0) {
            size_t pos = s.find("83928");
            int length = stoi(s.substr(0, pos));
            int num_size = s.substr(0, pos).size();
            decoded_strings.push_back(s.substr(num_size+5, length));
            s = s.substr(num_size+5+length);
        }

        return decoded_strings;
    }
};
