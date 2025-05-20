import pandas as pd
import sqlite3

# Connect to the Chinook database
conn = sqlite3.connect('chinook.db')

# 1. Customer Purchase Analysis
# Query to get total amount spent by each customer (from invoices)
query1 = '''
SELECT c.CustomerId, c.FirstName, c.LastName, SUM(i.Total) as TotalSpent
FROM customers c
JOIN invoices i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId, c.FirstName, c.LastName
ORDER BY TotalSpent DESC
LIMIT 5
'''
top_customers = pd.read_sql_query(query1, conn)
print("1. Top 5 Customers by Total Amount Spent:")
print(top_customers)

# 2. Album vs. Individual Track Purchases
# Step 1: Get all tracks per album
album_tracks = pd.read_sql_query('''
SELECT AlbumId, COUNT(*) as TrackCount
FROM tracks
GROUP BY AlbumId
''', conn)

# Step 2: Get customer purchases (invoice lines)
purchases = pd.read_sql_query('''
SELECT il.InvoiceId, il.TrackId, t.AlbumId
FROM invoice_items il
JOIN tracks t ON il.TrackId = t.TrackId
''', conn)

# Step 3: Get invoice to customer mapping
invoices = pd.read_sql_query('''
SELECT InvoiceId, CustomerId
FROM invoices
''', conn)

# Merge purchases with invoices to get customer info
purchases = purchases.merge(invoices, on='InvoiceId')

# Step 4: For each customer, count tracks bought per album
customer_album_purchases = purchases.groupby(['CustomerId', 'AlbumId']).size().reset_index(name='TracksBought')

# Merge with album_tracks to compare tracks bought vs total tracks in album
customer_album_purchases = customer_album_purchases.merge(album_tracks, on='AlbumId')

# Step 5: Determine if a purchase is a "full album" (all tracks bought) or "individual tracks" (subset of tracks)
customer_album_purchases['PurchaseType'] = customer_album_purchases.apply(
    lambda x: 'Full Album' if x['TracksBought'] == x['TrackCount'] else 'Individual Tracks', axis=1
)

# Step 6: Classify customers based on their purchase preference
customer_purchase_types = customer_album_purchases.groupby('CustomerId')['PurchaseType'].agg(lambda x: x.mode()[0]).reset_index()

# Step 7: Calculate percentages
total_customers = len(customer_purchase_types)
individual_track_customers = len(customer_purchase_types[customer_purchase_types['PurchaseType'] == 'Individual Tracks'])
full_album_customers = len(customer_purchase_types[customer_purchase_types['PurchaseType'] == 'Full Album'])

percent_individual = (individual_track_customers / total_customers) * 100
percent_full_album = (full_album_customers / total_customers) * 100

print("\n2. Album vs. Individual Track Purchases:")
print(f"Percentage of customers preferring individual tracks: {percent_individual:.2f}%")
print(f"Percentage of customers preferring full albums: {percent_full_album:.2f}%")

# Close the connection
conn.close()