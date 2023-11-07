from helpers.scraper import Scraper
from helpers.csv_helper import get_data_from_csv
from helpers.listing_helper import update_listings
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


def run_auto_market_place():
    # Your code to run when the button is clicked
    scraper = Scraper('https://facebook.com')

    # Add login functionality to the scraper
    scraper.add_login_functionality(
        'https://facebook.com', 'svg[aria-label="Trang cá nhân của bạn"]', 'facebook')
    scraper.go_to_page('https://facebook.com/marketplace/you/selling')

    # Get data for item type listings from csvs/items.csv
    item_listings = get_data_from_csv('items')
    # Publish all of the items into the facebook marketplace
    update_listings(item_listings, 'item', scraper)

    # # Get data for vechile type listings from csvs/vechiles.csv
    # vehicle_listings = get_data_from_csv('vehicles')
    # # Publish all of the vehicles into the facebook marketplace
    # update_listings(vehicle_listings, 'vehicle', scraper)


def run_auto_share_market():
    # Your code to run when the button is clicked
    scraper = Scraper('https://facebook.com')

    # Add login functionality to the scraper
    scraper.add_login_functionality(
        'https://facebook.com', 'svg[aria-label="Trang cá nhân của bạn"]', 'facebook')
    scraper.go_to_page('https://facebook.com/marketplace/you/selling')


root = ttk.Window(themename="superhero")
root.title('Auto FB')
root.geometry('600x350')

title_font = ("Helvetica", 25)
lableWellcome = ttk.Label(
    text='Auto Facebook Version 1.0.0', bootstyle="default", font=title_font)
lableWellcome.pack(side='top', padx=20, pady=20)

separator1 = ttk.Separator(bootstyle="danger")
separator1.pack(side='top')
lable_title = ttk.Label(text="Chạy niêm yết market place")
lable_title.pack(side='top')
button_auto_market = ttk.Button(root, text="Run Auto Market Place",
                                bootstyle="success", command=run_auto_market_place)
button_auto_market.pack(side='top', padx=5, pady=10)

separator1 = ttk.Separator(bootstyle="danger")
separator1.pack(side='top')

lable_title = ttk.Label(text="Chạy auto share bài niêm yết lên nhóm")
lable_title.pack(side='top')
button_auto_market = ttk.Button(root, text="Run Auto Share Market Place",
                                bootstyle="primary", command=run_auto_share_market)
button_auto_market.pack(side='top', padx=5, pady=10)

root.mainloop()
