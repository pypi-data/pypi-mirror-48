//
// Created by Aleksandr Khvorov on 20/05/2019.
//

#include <iostream>
#include <vector>
#include <string>
//#include <interfaces/tokenizers/base_tokenizer.h>
//#include "../../../main/cpp/interfaces/tokenizers/base_tokenizer.h"
#include "../../../main/cpp/interfaces/tokenizers/char_tokenizer.h"
#include "../../../main/cpp/interfaces/vgram_builders/string_vgram.h"

using namespace std;
//using namespace vgram_core;

void test_basic() {
    cout << "start" << endl;
    vector<string> data = {"aaaaaababababaaaaba", "aaaaaaaab"};
    vgram_core::BaseTokenizer *tokenizer = new vgram_core::CharTokenizer();
    auto *vgram = new vgram_core::StringVGram(5, 1000, tokenizer, 0);
    vgram->fit(data);
    for (const auto &word : vgram->alphabet()) {
        cout << word << " ";
    }
    cout << endl;
}

//void test_load(const string &filename) {
//    cout << "start" << endl;
//    vector<string> data = {"aaaaaababababaaaaba", "aaaaaaaab"};
//    vgram_core::BaseTokenizer *tokenizer = new vgram_core::CharTokenizer();
//    auto *vgram = new vgram_core::StringVGram(5, 1000, tokenizer, 0);
//    vgram->fit(data);
//    vgram->save(filename);
//    std::shared_ptr<vgram_core::StringVGram> vgram2 = vgram_core::StringVGram::load(filename);
//    for (const auto &word : vgram2->alphabet()) {
//        cout << word << " ";
//    }
//    cout << endl;
//}

void test_result_freq() {
    cout << "start" << endl;
    vector<string> data = {"hello world", "a cat sat on the mat"};
    auto *vgram = new vgram_core::StringVGram(99, 100);
    vgram->fit(data);
    for (const auto &word : vgram->alphabet()) {
        cout << word << " ";
    }
    cout << endl;
}

class StringVGram : public vgram_core::StringVGram {
public:
    static StringVGram *load(const std::string &filename) {
//        return std::shared_ptr<StringVGram>(dynamic_cast<StringVGram *>(vgram_core::StringVGram::load(filename).get()));
//        return std::static_pointer_cast<StringVGram>(vgram_core::StringVGram::load(filename));
        vgram_core::StringVGram *pGram = vgram_core::StringVGram::load(filename);
        StringVGram *gram = static_cast<StringVGram *>(pGram);
        return gram;
    }

    StringVGram(int size, int iter_num) : vgram_core::StringVGram(size, iter_num) {}

//    StringVGram *fit(const std::vector<std::string> &seqs) {
//        return dynamic_cast<StringVGram *>(vgram_core::StringVGram::fit(seqs));
//    }
//
//    std::vector<std::string> transform(const std::vector<std::string> &seqs) const {
//        return vgram_core::StringVGram::transform(seqs);
//    }
};

void test_py_load(const string &filename) {
    cout << "start" << endl;
    vector<string> data = {"aaaaaababababaaaaba", "aaaaaaaab"};
    auto *vgram = new StringVGram(5, 100);
    vgram->fit(data);
    vgram->save(filename);
    StringVGram* vgram2 = StringVGram::load(filename);
    for (const auto &word : vgram2->alphabet()) {
        cout << word << " ";
    }
    cout << endl;
}

int main() {
    string filename = "/Users/akhvorov/code/mlimlab/vgram/vgram/core/src/test/cpp/interfaces/dict.json";
    test_py_load(filename);
    cout << "in main" << endl;
    return 0;
}
