# GpxMod Nextcloud アプリ

GPS トラックファイルの表示、解析、比較、共有。

🌍 [GpxPod Crowdin プロジェクト](https://crowdin.com/project/gpxpod) でこのアプリを翻訳する手助けをしてください。

GpxPod :

* 🗺 can display gpx/kml/tcx/igc/fit files anywhere in your files, files shared with you, files in folders shared with you. fit ファイルは、サーバシステムに **GpsBabel** があった場合にのみ変換・表示されます
* 📏 メートル法、ヤードポンド法、航海測定システムをサポートしています
* 🗠 draws elevation, speed or pace interactive chart
* 🗠 can color track lines by speed, elevation or pace
* 🗠 show track statistics
* ⛛ filter tracks by date, total distance...
* 🖻 displays geotagged pictures found in selected directory
* 🖧 generates public links pointing to a track/folder. This link can be used if the file/folder is shared by public link
* 🗁 allows you to move selected track files
* 🗠 can correct tracks elevations if SRTM.py (gpxelevations) is found on the server's system
* ⚖ can make global comparison of multiple tracks
* ⚖ can make visual pair comparison of divergent parts of similar tracks
* 🀆 allows users to add personal map tile servers
* ⚙ saves/restores user options values
* 🖍 allows user to manually set track line colors
* 🕑 ブラウザのタイムゾーンを検出
* 🗬 インストールされている場合、GpxEditから追加のマーカー記号を読み込みます
* 🔒 暗号化されたデータフォルダ（サーバー側の暗号化）で動作します
* 🍂 proudly uses Leaflet with lots of plugins to display the map
* 🖴 is compatible with SQLite, MySQL and PostgreSQL databases
* 🗁 adds possibility to view .gpx files directly from the "Files" app

このアプリは、Firefox 57+ と Chromium で NextCloud 15 でテストされていった。

このアプリは(遅い)開発中です。

Nextcloudアプリケーションのウェブサイトへのリンク : https://apps.nextcloud.com/apps/gpxpod

## インストール

インストールの詳細は [AdminDoc](https://gitlab.com/eneiluj/gpxpod-oc/wikis/admindoc) を参照してください。

## 既知の問題

* 単引用符又は二重引用符を含むファイル名の管理が悪い
* *警告*, kml 変換は、私有の "gx:track" 拡張タグを使用した最近の kml ファイルには動作できません。

ご意見をいただければ幸いです。