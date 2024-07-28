import requests
from bs4 import BeautifulSoup


class ScraperException(Exception):
    pass


class InvalidURLException(ScraperException):
    pass


class DataFetchingException(ScraperException):
    pass


def scrape_website(url, filename):
    try:
        # Validate URL
        if not url.startswith("http://") and not url.startswith("https://"):
            raise InvalidURLException(
                " Please provide a valid URL starting with http:// or https://"
            )

        # Make HTTP request
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Parse the content
        soup = BeautifulSoup(response.content, "html.parser")
        data = soup.get_text(separator="\n")  # Extract all text from the HTML

        # Write data to the file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)

        print(f"Data successfully written to {filename}")

    except InvalidURLException as e:
        print(f"Invalid URL error: {e}")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")

    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")

    except requests.exceptions.Timeout as e:
        print(f"Timeout error: {e}")

    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")

    except IOError as e:
        print(f"IO error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    else:
        print("Scraping and file writing completed without any exceptions.")

    finally:
        print("Scraping process finished, performing cleanup if necessary.")


file_path = (
    "C:/Users/ashritha.shankar/python/python/template_project/src/"
    "template_project/error_handling/scraped_data.json"
)

if __name__ == "__main__":
    url = "https://www.scrapethissite.com/"
    filename = file_path
    scrape_website(url, filename)
