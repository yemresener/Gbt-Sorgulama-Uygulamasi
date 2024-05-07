-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 07 May 2024, 22:10:41
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `python_gbt`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `halk`
--

CREATE TABLE `halk` (
  `tc` text NOT NULL,
  `isim_soyisim` text NOT NULL,
  `dogum_tarih` text NOT NULL,
  `dogum_yer` text NOT NULL,
  `ana` text NOT NULL,
  `baba` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `halk`
--

INSERT INTO `halk` (`tc`, `isim_soyisim`, `dogum_tarih`, `dogum_yer`, `ana`, `baba`) VALUES
('57978365808', 'Adem Kaya', '19.02.1990', 'İstanbul', 'Gamze', 'Ahmet'),
('82180168510', 'Emine Sarı\r\n', '01.01.1999', 'Ankara', 'Ayşe', 'Mahmut'),
('58658723802', 'Süleyman Erdoğan\r\n', '11.09.1976', 'Edirne', 'Hatice', 'Mehmet'),
('40721120120', 'Recep Kaya\r\n', '11.11.2001', 'İstanbul', 'Sıla', 'Haydar'),
('35490603134', 'Emine Öztürk\r\n', '07.06.2000', 'Ankara', 'Ömür', 'Halim'),
('81507122556', 'Şaban Sarı\r\n', '09.12.1995', 'İstanbul', 'Hayriye', 'Osman'),
('40675490140', 'Muhammed Aktaş\r\n', '17.11.1983', 'Iğdır', 'Aslı', 'Eren'),
('72063751540', 'Sibel Güneş\r\n', '11.09.1977', 'Hatay', 'Ümmü', 'Müslüm'),
('81176696082', 'Mehmet Özkan\r\n', '09.12.2000', 'Ankara', 'Melike', 'Aslan'),
('15554239790', 'İsmail Doğan\r\n', '06.12.1999', 'Hakkari', 'Ayşe', 'Müslüm'),
('68280286774', 'Hacer Özkan\r\n', '12.12.2002', 'Adıyaman', 'Gamze', 'Ali'),
('30738999086', 'Cemal Polat\r\n', '05.12.1989', 'Ağrı', 'Ayşe', 'Mehmet'),
('97252458024', 'Yunus Işık\r\n', '12.11.1989', 'İstanbul', 'Yeter', 'Kazım'),
('63335620244', 'Hüseyin Kılıç\r\n', '03.01.2004', 'İstanbul', 'İrem', 'İsmail'),
('41896899576', 'Döndü Taş\r\n', '09.12.1999', 'İstanbul', 'Hayriye', 'Hayri'),
('65587492556', 'Leyla Güler\r\n', '01.12.1978', 'İstanbul', 'Alime', 'Mehmet'),
('42633491800', 'Fatma Çetin\r\n', '09.05.1993', 'İstanbul', 'Tuğçe', 'İsmail'),
('72597003306', 'Zehra Şimşek\r\n', '09.11.2003', 'İstanbul', 'Pelin', 'Umut'),
('51052246038', 'Muhammet Yavuz\r\n', '30.11.2000', 'İstanbul', 'Esma', 'Mehmet'),
('13858860740', 'Fadime Özdemir\r\n', '09.01.1998', 'İstanbul', 'Melek', 'Hüseyin'),
('85219769276', 'Kadriye Can\r\n', '06.11.1997', 'İstanbul', 'Şebnem', 'Muhammet');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `polisler`
--

CREATE TABLE `polisler` (
  `id` int(11) NOT NULL,
  `tc` text NOT NULL,
  `sifre` text NOT NULL,
  `dogrulama` text NOT NULL,
  `isim` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `polisler`
--

INSERT INTO `polisler` (`id`, `tc`, `sifre`, `dogrulama`, `isim`) VALUES
(1, '1', '1', 'emre', 'Yunus Emre Şener');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `suc`
--

CREATE TABLE `suc` (
  `tc` text NOT NULL,
  `sucu` text NOT NULL,
  `suc_yeri` text NOT NULL,
  `suc_tarih` text NOT NULL,
  `ceza` text NOT NULL,
  `durum` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Tablo döküm verisi `suc`
--

INSERT INTO `suc` (`tc`, `sucu`, `suc_yeri`, `suc_tarih`, `ceza`, `durum`) VALUES
('82180168510', 'Hırsızlık', 'İstanbul-Avcılar', '12.07.2023', 'para cezası', '-'),
('57978365808', 'Kaçakçılık‎ ', 'İstanbul-Şişli', '12.07.2023', 'Hapis', '-'),
('58658723802', 'Bilişim suçları‎', 'İstanbul-Bağcılar', '11.02.2022', 'Para cezası', '-'),
('40721120120', 'Soygun‎', 'İstanbul-Esenler', '09.12.2022', 'Hapis', 'Aranıyor'),
('35490603134', 'Soygun‎', 'İstanbul-Esenler', '09.12.2022', 'Hapis', 'Aranıyor'),
('81507122556', 'Terörizm', 'İstanbul-Taksim', '01.05.2024', 'Hapis', 'Aranıyor'),
('40675490140', 'Polise şiddet', 'İstanbul-Esenyurt', '01.05.2024', 'Para cezası', 'Aranıyor'),
('72063751540', 'Hırsızlık‎', 'İstanbul-Bağcılar', '03.05.2024', 'Para cezası', '-'),
('81176696082', 'Hayvana Şiddet', 'İstanbul-Kadiköy', '12.05.2024', 'Para cezası', '-'),
('15554239790', 'Gasp', 'İstanbul-Beşiktaş', '12.05.2024', 'Para cezası', '-'),
('68280286774', 'Cinayet', 'İstanbul-Beyoğlu', '02.05.2024', 'Hapis', 'Aranıyor'),
('30738999086', 'Hırsızlık', 'İstanbul-Esenler', '01.04.2024', 'Para cezası', '-'),
('97252458024', 'Yolsuzluk', 'İstanbul-Başakşehir', '12.04.2024', 'Hapis', 'Aranıyor'),
('63335620244', 'Hakaret', 'İstanbul-Kadıköy', '12.02.2024', 'Para cezası', '-'),
('41896899576', 'Gasp', 'İstanbul-Esenler', '11.12.2023', 'Para cezası', '-'),
('65587492556', 'Holiganlık‎ ', 'İstanbul-Taksim', '1.05.2023', 'Para cezası', '-'),
('42633491800', 'Holiganlık‎ ', 'İstanbul-Taksim', '01.05.2023', 'Para cezası', '-'),
('72597003306', 'Soygun', 'İstanbul-Fatih', '12.09.2023', 'Hapis', 'Aranıyor'),
('51052246038', 'Kaçakçılık‎ ', 'İstanbul-Avcılar', '12.02.2022', 'Hapis', '-'),
('13858860740', 'Gasp', 'İstanbul-Bağcılar', '12.01.2022', 'Para cezası', '-'),
('85219769276', 'Hayvana şiddet', 'İstanbul-Esenyurt', '12.01.2019', 'Para cezası', '-'),
('81507122556', 'Holiganlık', 'İstanbul-Taksim\r\n', '01.05.2022', 'Para cezası', '-'),
('35490603134', 'Gasp', '01.02.2020', 'İstanbul-Esenler', 'Para cezası', '-'),
('15554239790', 'Hırsızlık', 'İstanbul-Beşiktaş', '01.07.2023', 'Para cezası', '-'),
('68280286774', 'Hayvana şiddet', 'İstanbul-Beyoğlu', '04.01.2023', 'Para cezası', '-'),
('30738999086', 'Gasp', 'İstanbul-Esenler', '17.02.2023', 'Para cezası', '-'),
('13858860740', 'Gasp', 'İstanbul-Esenler', '30.03.2024', 'Para cezası', '-'),
('82180168510', 'Gasp', 'İstanbul-Avcılar\r\n', '12.01.2021\r\n', 'Para cezası', '-');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `polisler`
--
ALTER TABLE `polisler`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `polisler`
--
ALTER TABLE `polisler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
