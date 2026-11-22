# import de la bibliotheque yfinance 
import yfinance as yf

def get_stock_prices(symbol): 
    # selection de l'action symbol choisis
    ticker = yf.Ticker(symbol)
    
    history = ticker.history(
        period="1y", # demande d'un an historique
        interval="1d", # observation par seance boursière
        auto_adjust=True # ajuster les prix pour tenir compte des splits et dividendes
    )

    return history

if __name__ == "__main__":
    df = get_stock_prices("MSFT")
    print(df.tail())