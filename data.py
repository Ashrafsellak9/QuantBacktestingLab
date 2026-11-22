# import de la bibliotheque yfinance 
import yfinance as yf
# selection de l'action Apple
ticker = yf.Ticker("AAPL")

history = ticker.history(
    period="1y", # demande d'un an historique
    interval="1d", # observation par seance boursiere
    auto_adjust=True # ajuster les prix pour tenir compte des splits et dividendes
)
# affichage des 5 dernieres lignes
print(history.tail()) 