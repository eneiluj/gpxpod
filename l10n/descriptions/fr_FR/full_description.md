# Application Nextcloud GpxPod

Afficher, analyser, comparer et partager des fichiers de traces GPS.

🌍 Aidez-nous à traduire cette application sur [le project Crowdin Nextcloud Gpxpod](https://crowdin.com/project/gpxpod).

GpxPod:

* 🗺  can display gpx/kml/tcx/igc/fit files anywhere in your files, files shared with you, files in folders shared with you
* 📏 supporte les systèmes de mesure métriques, anglais et nautique
* 🗠 dessine un graphique interactif d'altitude, de vitesse ou de rythme
* 🗠 peut colorier les lignes des traces en fonction de la vitesse, de l'altitude ou du rythme
* affiche les statistiques des traces
* 🖻  displays geotagged pictures
* 🖧 génère des liens publics vers un fichier/dossier. Ce lien peut être utilisé si le fichier/dossier est partagé par un lien public
* 🗁 vous permet de déplacer les fichiers de piste sélectionnés
* 🗠 peut corriger les altitudes des traces si SRTM.py (gpxelevations) est trouvé sur le système du serveur
* ⚖ peut faire une comparaison globale de plusieurs traces
* ⚖ peut faire une comparaison visuelle de parties divergentes de paires de traces similaires
* 🀆 permet aux utilisateurs d'ajouter des serveurs personnels de tuiles de carte
* ⚙ sauvegarde/restaure les valeurs d'options de l'utilisateur
* 🖍 permet à l'utilisateur de définir manuellement la couleur des traces
* 🕑 détecte le fuseau horaire du navigateur
* 🗬 charge les symboles de marqueur supplémentaires de GpxEdit si installé
* 🔒 fonctionne avec un dossier de données chiffré (chiffrement côté serveur)
* 🍂 utilise fièrement Leaflet avec plein de plugins pour afficher la carte
* 🖴 est compatible avec les bases de données SQLite, MySQL et PostgreSQL
* 🗁 ajoute la possibilité de voir les fichiers .gpx directement à partir de l'application "Fichiers"

Cette application a était testée sur Nextcloud 15 avec Firefox 57+ et Chromium.

Cette appli est en développement (lent).

Lien vers le site des applications Nextcloud : https://apps.nextcloud.com/apps/gpxpod

## Installation

Voir l' [AdminDoc](https://gitlab.com/eneiluj/gpxpod-oc/wikis/admindoc) pour les détails sur l'installation

## Problèmes connus

* *ATTENTION*, la conversion kml ne fonctionnera PAS avec les fichiers kml récents utilisant le tag propriétaire "gx:track".

Tout retour sera apprécié.
