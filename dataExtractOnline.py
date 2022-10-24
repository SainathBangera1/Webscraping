# Necessary imports
import sys
import urllib.request

# Save a reference to the original
# standard output
original_stdout = sys.stdout

# as an example, taken my article list
# published link page and stored in local
for i in range(2009, 2023):
    with urllib.request.urlopen('https://www.superenalotto.net/en/results/'+str(i)) as webPageResponse:
        outputHtml = webPageResponse.read()
    # Scraped contents are placed in
    # samplehtml.html file and getting
    # used for next set of examples
    # with open('data.html', 'w') as f:
    with open('htmlData/'+str(i)+'.html', 'w') as f:

        # Here the standard output is
        # written to the file that we
        # used above
        sys.stdout = f
        print(outputHtml)

        # Reset the standard output to its
        # original value
        sys.stdout = original_stdout
print("Data extracted and ready to use...")
