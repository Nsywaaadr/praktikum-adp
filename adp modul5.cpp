#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int n;
    cout << "Banyak Data n: ";
    cin >> n;

    vector<double> x_nilai, f_nilai, g_nilai, h_nilai;

    for (int i = 0; i < n; ++i) {
        double x;
        cout << "Nilai x_" << i + 1 << ": ";
        cin >> x;

        x_nilai.push_back(x);

        double f;
        if (x >= 0) {
            f = 3 * x * x + 7 * x - 2;
        }
        if (x <= 0) {
            f = 2 * x * x - 5 * x - 4;
        }
        f_nilai.push_back(f);

        double g = f * f - x * 0.5;
        g_nilai.push_back(g);

        double h = f * g;
        h_nilai.push_back(h);
    }

    cout << "\nFungsi Nilai F(x):" << endl;
    for (int i = 0; i < n; ++i) {
        cout << "F(x_" << i + 1 << ") = " << fixed << f_nilai[i] << endl;
    }

    cout << "\nFungsi Nilai G(x):" << endl;
    for (int i = 0; i < n; ++i) {
        cout << "G(x_" << i + 1 << ") = " << fixed << g_nilai[i] << endl;
    }

    cout << "\nFungsi Nilai H(x):" << endl;
    for (int i = 0; i < n; ++i) {
        cout << "H(x_" << i + 1 << ") = " << fixed << h_nilai[i] << endl;
    }

    return 0;
}
