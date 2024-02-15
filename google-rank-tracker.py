#google serch websitelink
from googlesearch import search

def get_all_google_search_results(keyword, num_results=90):
    search_results = []

    # Perform a Google search for the specified keyword
    for result in search(keyword, num_results=num_results):
        search_results.append(result)

    return search_results

def extract_website_links(search_results):
    website_links = []

    for result in search_results:
        # Extract the domain from the URL
        domain = result.split('//')[-1].split('/')[0]
        website_links.append(domain)

    return website_links

def get_related_sites(keyword, num_results=30):
    related_sites = []

    # Add terms like "related" to the search query to find similar sites
    related_query = f"{keyword} related"

    # Perform a Google search for related sites
    for result in search(related_query, num_results=num_results):
        related_sites.append(result)

    return related_sites

# Replace 'your_keyword' with the specific keyword you're interested in
keyword_for_search = 'enter your keyword'

# Add related terms to the search query
related_terms = ['enter your related_term-1', 'enter your related_term-2']  # Add more terms as needed

# Combine the main keyword with related terms for a broader search
combined_query = f"{keyword_for_search} {' '.join(related_terms)}"

# Get all Google search results for the specified keyword and related terms
all_results = get_all_google_search_results(combined_query)

if all_results:
    print(f"All websites from Google search results for '{combined_query}':")
    website_links = extract_website_links(all_results)
    for link in website_links:
        print(link)

    # Get related sites
    related_sites = get_related_sites(keyword_for_search)
    if related_sites:
        print("\nRelated sites:")
        for site in related_sites:
            print(site)
    else:
        print("No related sites found.")
else:
    print("No search results found.")
