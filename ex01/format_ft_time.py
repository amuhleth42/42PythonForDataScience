from datetime import datetime
import time

timestamp = time.time()
epoch = datetime(1970, 1, 1)
date = datetime.now().strftime('%b %d %Y')
scientific_notation = "{:.2e}".format(timestamp)

print(f"Seconds since {epoch}: {timestamp:,.4f} or {scientific_notation} in scientific notation")
print(date)
