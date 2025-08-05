# Algebra_clustering

Il codice è composto da 4 classi e un main. I dataset sono locati nella cartella "Datasets" e sono consultabili.
Il main contiene una voce "dataset" in cui va inserito il nome del dataset come riportato nella cartella "Datasets". 
Inoltre, sono presenti dei controlli: k per decidere l'intorno di esplorazione (10,20,40) mentre gli others sono 
per mostrare graficamente gli altri metodi di clusters (settare su "False" se non si vogliono vedere).

Il tasto interactive può essere settato su "True" cos' da poter inserire sul terminale i parametri richiesti, quindi:
- scelta del metodo di calcolo degli eigenvalues tra shifting e deflation
- scelta del metodo di calcolo degli eigenvectors tra shifting e deflation
- scelta del numero di clusters
- scelta del raggio eps per il DBscan

Se invece interactive è fissato a "False", verrà lanciato il codice del dataset indicato nella voce "dataset" in modalità default.
