# roop for StableDiffusion/roop untuk StableDiffusion

(English)
This is an extension for StableDiffusion's [AUTOMATIC1111 web-ui](https://github.com/P2Enjoy/stable-diffusion-webui/) that allows face-replacement in images. It is based on [roop](https://github.com/s0md3v/roop) but will be developed seperately.

(Indonesia
Ini adalah ekstensi untuk [AUTOMATIC1111 web-ui] (https://github.com/P2Enjoy/stable-diffusion-webui/) milik StableDiffusion yang memungkinkan penggantian wajah pada gambar. Ini didasarkan pada [roop] (https://github.com/s0md3v/roop) tetapi akan dikembangkan secara terpisah.)
![example](example/example.png)


### Disclaimer/Penyangkalan

(English)
This software is meant to be a productive contribution to the rapidly growing AI-generated media industry. It will help artists with tasks such as animating a custom character or using the character as a model for clothing etc.

The user of this software are aware of its possible unethical applicaitons and are committed to take preventative measures against them.

Users of this software are expected to use this software responsibly while abiding the local law. If face of a real person is being used, users are suggested to get consent from the concerned person and clearly mention that it is a deepfake when posting content online. Developers of this software will not be responsible for actions of end-users.

(Indonesia)
Perangkat lunak ini dimaksudkan untuk menjadi kontribusi yang produktif bagi industri media yang dihasilkan oleh AI yang berkembang pesat. Perangkat lunak ini akan membantu para seniman dalam melakukan tugas-tugas seperti menganimasikan karakter khusus atau menggunakan karakter tersebut sebagai model pakaian, dll.

Pengguna perangkat lunak ini menyadari kemungkinan aplikasi yang tidak etis dan berkomitmen untuk mengambil tindakan pencegahan terhadapnya.

Pengguna perangkat lunak ini diharapkan untuk menggunakan perangkat lunak ini secara bertanggung jawab dan mematuhi hukum setempat. Jika menggunakan wajah orang sungguhan, pengguna disarankan untuk mendapatkan persetujuan dari orang yang bersangkutan dan dengan jelas menyebutkan bahwa itu adalah pemalsuan saat memposting konten secara online. Pengembang perangkat lunak ini tidak bertanggung jawab atas tindakan pengguna akhir.

## Installation/Pemasangan
(English)
First of all, if you can't install it for some reason, don't open an issue here. Google your errors.

To install the extension, follow these steps:

+ Run this command: `pip install insightface==0.7.3`
+ In web-ui, go to the "Extensions" tab and use this URL `https://github.com/vorstcavry` in the "install from URL" tab.
+ Close webui and run it again
+ If you encounter `'NoneType' object has no attribute 'get'` error, download the [inswapper_128.onnx](https://huggingface.co/henryruhs/roop/resolve/main/inswapper_128.onnx) model and put it inside `<webui_dir>/models/roop/` directory.

On Windows.. just use linux: you're grown up enough to get to serious stuff instead of playing with baby's toys.
For rest of the errors, use google. Good luck.

(Indonesia)
Pertama-tama, jika Anda tidak dapat menginstalnya karena suatu alasan, jangan membuka masalah di sini. Cari kesalahan Anda di Google.

Untuk menginstal ekstensi, ikuti langkah-langkah berikut:

+ Jalankan perintah ini: `pip install insightface==0.7.3`
+ Pada web-ui, buka tab "Extensions" dan gunakan URL ini `https://github.com/vorstcavry` pada tab "instal dari URL".
+ Tutup webui dan jalankan kembali
+ Jika Anda menemukan kesalahan `'NoneType' objek tidak memiliki atribut 'get'`, unduh model [inswapper_128.onnx](https://huggingface.co/henryruhs/roop/resolve/main/inswapper_128.onnx) dan letakkan di dalam direktori `<webui_dir>/models/roop/`.

Pada Windows... gunakan saja linux: Anda sudah cukup dewasa untuk melakukan hal-hal yang serius daripada bermain dengan mainan bayi.
Untuk kesalahan lainnya, gunakan google. Semoga berhasil.

## Usage/Penggunaan

(English)

1. Under "roop" drop-down menu, import an image containing a face.
2. Turn on the "Enable" checkbox
3. That's it, now the generated result will have the face you selected

(Indonesia)

1. Di bawah menu tarik-turun "roop", impor gambar yang berisi wajah.
2. Aktifkan kotak centang "Aktifkan"
3. Selesai, sekarang hasil yang dihasilkan akan memiliki wajah yang Anda pilih
## Tips

### The result face is blurry/Hasil wajah menjadi buram

(English)

Use the "Restore Face" option. You can also try the "Upscaler" option or for more finer control, use an upscaler from the "Extras" tab.

(Indonesia)

Gunakan opsi "Restore Face". Anda juga bisa mencoba opsi "Upscaler" atau untuk kontrol yang lebih halus, gunakan upscaler dari tab "Extras".

### There are multiple faces in result/Terdapat beberapa wajah dalam hasilnya

(English)

Select the face numbers you wish to swap using the "Comma separated face number(s)" option.

(Indonesia)

Pilih nomor wajah yang ingin Anda tukar dengan menggunakan opsi "Nomor wajah yang dipisahkan koma".

#### Getting good quality results/Mendapatkan hasil yang berkualitas bagus

(English)

First of all, make sure the "Restore Face" option is enabled. You can also try the "Upscaler" option or for more finer control, use an upscaler from the "Extras" tab.

For even better quality, use img2img with denoise set to `0.1` and gradually increase it until you get a balance of quality and resembelance.

(Indonesia)

Pertama-tama, pastikan opsi "Restore Face" diaktifkan. Anda juga bisa mencoba opsi "Upscaler" atau untuk kontrol yang lebih halus, gunakan upscaler dari tab "Extras".

Untuk kualitas yang lebih baik lagi, gunakan img2img dengan denoise yang ditetapkan ke `0.1` dan secara bertahap tingkatkan sampai Anda mendapatkan keseimbangan kualitas dan kemiripan.

#### Replacing specific faces/Mengganti wajah tertentu

(English)

If there are multiple faces in an image, select the face numbers you wish to swap using the "Comma separated face number(s)" option.

()



#### The face didn't get swapped?

(English)

Did you click "Enable"?

If you did and your console doesn't show any errors, it means roop detected that your image is either NSFW or wasn't able to detect a face at all.

### Img2Img

(English)

You can choose to activate the swap on the source image or on the generated image, or on both using the checkboxes. Activating on source image allows you to start from a given base and apply the diffusion process to it.

Inpainting should work but only the masked part will be swapped.
