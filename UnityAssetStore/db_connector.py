import sqlite3

con = sqlite3.connect('assets_repos.db')
cur = con.cursor()

"""
Editors:
    Add an asset
    Edit an asset
    Remove an asset
    
    Add a repo
    Edit a repo
    Remove a repo
    
    Add a keyword
    Edit a keyword
    Remove a keyword
    
    Add an asset,repo pair
    Edit an asset,repo pair
    Remove an asset,repo pair
    
Queries:
    All assets in [repo]
    Filter assets by keywords
    
Sample prepared statements
    cur.execute("insert into lang values (?, ?)", ("C", 1972))
    
    cur.execute("select * from lang where first_appeared=:year",{"year": 1972})
    
    lang_list = [("Fortran", 1957), ("Python", 1991), ("Go", 2009)]
    cur.executemany("insert into lang values (?, ?)", lang_list)
"""
 #TODO - Move functions around to prevent errors
 
#==============================================================================
#                                   Adders
#==============================================================================
"""
Add an asset to Asset_Info
Parameter format:
    asset_id
    name
    link
    description
    date
    meta_data
    image (link)
    entity_extension (1 for entity, 0 for extension)
"""
def add_asset(a_id, name, link, desc, date, meta, imgl, enex): #TODO
    cur.execute("INSERT INTO Asset_Info VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (a_id, name, link, desc, date, meta, imgl, enex))

"""
Add a list of keywords/filters to an asset
Parameter format:
    asset_id
    array/list of keywords
"""
def add_asset_keywords(a_id, keywords): #TODO
    for word in keywords:
        cur.execute("INSERT INTO Asset_Keyword VALUES (?, ?)", (a_id, word))

"""
Create a new repo
Parameter format:
    repo_key
    name of repo
    email of creator
"""
def add_repo(r_key, name, email): #TODO
    return 0

"""
Add asset to a repo
Parameter format:
    asset_id
    repo_key
"""
def add_asset_to_repo(a_id, r_key): #TODO
    return 0

#==============================================================================
#                                   Removers
#==============================================================================

"""
Remove an asset from the master list of assets
Parameter format:
    asset_id
"""
def remove_asset(a_id): #TODO
    return 0

"""
Remove all assets from repo, then delete the repo
Parameter format:
    repo_key
"""
def remove_repo(r_key): #TODO
    return 0

"""
Remove a keyword from a specified asset
Parameter format:
    asset_id
    keyword
"""
def remove_keyword(a_id, keyword): #TODO
    return 0

"""
Remove an asset from a repo, if the asset was only in that repo, remove asset from master list
Parameter format:
    asset_id
    repo_key
"""
def remove_asset_from_repo(a_id, r_key): #TODO
    return 0

#==============================================================================
#                                   Editors
#==============================================================================

 #TODO

#==============================================================================
#                                   Getters
#==============================================================================

 #TODO

#==============================================================================
#                               Check if Exists
#==============================================================================

"""
Check if asset exists in master list
Parameter format:
    asset_id
"""
def does_asset_exist(a_id): #TODO
    return 0

"""
Check if repo exists
Parameter format:
    repo_key
"""
def does_repo_exist(r_key): #TODO
    return 0

"""
Check if a keyword is associated with an asset
Parameter format:
    asset_id
    keyword
"""
def does_asset_keyword_exist(a_id, keyword): #TODO
    return 0

"""
Check if an asset is part of a repo
Parameter format:
    asset_id
    repo_key
"""
def does_asset_exist_in_repo(a_id, r_key): #TODO
    return 0

#==============================================================================
#                                   Main
#==============================================================================

for row in cur.execute("SELECT asset_id,name FROM Asset_Info;"):
    print(row)
#print(cur.fetchall())