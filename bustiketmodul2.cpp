#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
  map<string, int> harga_tiket = {
    {"Medan", 365000},
    {"Padang", 250000},
    {"Bengkulu", 285000},
    {"Jambi", 265000},
    {"Pekanbaru", 150000},
    {"Lampung", 453000}
  };

  cout << "Nama: Nasywa Adila Rahma" << endl;
  cout << "Nim: 2310433022" << endl;
  cout << "SHIFT 2" << endl;
  cout << "-----------------------------------" << endl;
  cout << "Bus PT. ANS lintas sumatera" << endl;
  string tujuan_dipesan;
  cout << "Tujuan yang dipesan: ";
  cin >> tujuan_dipesan;
  if (tujuan_dipesan != "Medan" && tujuan_dipesan != "Padang" && tujuan_dipesan != "Bengkulu" && tujuan_dipesan != "Jambi" && tujuan_dipesan != "Pekanbaru" && tujuan_dipesan != "Lampung") {
    cout << "Tujuan bus yang dipesan tidak valid." << endl;
    return 0;
  }
  cout << "----------------------------------------------" << endl;
  cout << "kelas (biaya tambahan)" << endl;
  int economi_class = 10000;
  int bisnis_class = 20000;
  int first_class = 30000;
  cout << "Economi Class: " << economi_class << endl;
  cout << "Bisnis Class: " << bisnis_class << endl;
  cout << "First Class: " << first_class << endl;
  string kelas_dipesan;
  cout << "kelas yang diambil: ";
  cin >> kelas_dipesan;
  int harga_kelas;
  if (kelas_dipesan == "Ekonomi") {
    harga_kelas = economi_class;
  } else if (kelas_dipesan == "Bisnis") {
    harga_kelas = bisnis_class;
  } else if (kelas_dipesan == "First") {
    harga_kelas = first_class;
  } else {
    cout << "kelas bus yang dipesan tidak valid" << endl;
    return 0;
  }
  int jumlah_tiket;
  cout << "Masukkan jumlah tiket yang dipesan untuk tujuan " << tujuan_dipesan << ": ";
  cin >> jumlah_tiket;
  int total_harga = jumlah_tiket * harga_tiket[tujuan_dipesan];
  total_harga += jumlah_tiket * harga_kelas;

  int diskon;
  if (jumlah_tiket < 5) {
    diskon = harga_tiket[tujuan_dipesan] * 0.05;
  } else if (jumlah_tiket > 5) {
    diskon = harga_tiket[tujuan_dipesan] * 0.1;
  } else {
    diskon = 0;
  }

  int total_harga_setelah_diskon = total_harga - diskon;
  cout << "Tujuan: " << tujuan_dipesan << endl;
  cout << "Kelas: " << kelas_dipesan << endl;
  cout << "Jumlah tiket: " << jumlah_tiket << endl;
  cout << "Total harga tiket untuk " << jumlah_tiket << " tiket ke " << tujuan_dipesan << " dengan kelas " << kelas_dipesan << " adalah Rp. " << total_harga << endl;
  cout << "diskon yang diberikan adalah Rp. " << diskon << endl;
  cout << "total harga tiket setelah diskon adalah Rp. " << total_harga_setelah_diskon << endl;

  return 0;
}
