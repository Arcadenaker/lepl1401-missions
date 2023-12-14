from mission9 import Article, Facture, ArticlePiece, Piece, ArticleReparationUrgente

articles = [ Article("laptop 15\" 8GB RAM", 743.79),
             Article("installation windows", 66.11),
             Article("installation wifi", 45.22),
             Article("carte graphique", 119.49),
             ArticleReparationUrgente(3),
             ]

articles2 = [ArticlePiece(1, Piece("disque dur 350 GB",49.99, 0.355, True)), 
             ArticlePiece(3, Piece("souris bluetooth",15.99, 0.176)), 
             ArticlePiece(5, Piece("adaptateur DVI - VGA",12.00, 0)), 
             ArticlePiece(2, Piece("Java in a Nutshell",24.00, 0.321, TVA_reduit=True)), # TVA_reduit applique une tva de 6% au lieu de 21% comme le demande l'énoncé
             ArticlePiece(5, Piece("souris bluetooth",15.99, 0.176))]

def test_articles(a_list) :
    for art in a_list :
        print(art)

facture = Facture("PC Store - 22 novembre", articles)
bordereau = Facture("PC Store - 22 novembre", articles2)


def test_facture(f) :
    print(f)

if __name__ == "__main__":

    print("\n*** AFFICHAGE DE LA CLASSE ARTICLE ***\n")
    test_articles(articles)

    print("\n*** TEST DE LA CLASSE Facture AVEC RÉPARATION D'URGENCE ***\n")
    test_facture(facture)

    print("\n*** TEST DE LA CLASSE Facture AVEC ArticlePiece, Piece, ArticleReparationUrgente ***\n")
    test_facture(bordereau)
    test_facture(bordereau.print_livraison())
