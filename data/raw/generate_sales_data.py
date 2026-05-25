{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "16d9e6dc-2483-4c83-a9a1-b6526ff86138",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ==========================================\n",
    "# SALES DATASET GENERATOR\n",
    "# ==========================================\n",
    "\n",
    "import pandas as pd\n",
    "import random\n",
    "from faker import Faker\n",
    "\n",
    "# Initialize faker\n",
    "fake = Faker()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5f0db82c-d02a-41bf-bb95-8469673e00da",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ==========================================\n",
    "# MASTER DATA\n",
    "# ==========================================\n",
    "\n",
    "customers = [\n",
    "    \"Infosys\",\n",
    "    \"TCS\",\n",
    "    \"Wipro\",\n",
    "    \"HCL\",\n",
    "    \"Tech Mahindra\",\n",
    "    \"Accenture\",\n",
    "    \"Capgemini\",\n",
    "    \"Cognizant\",\n",
    "    \"IBM\",\n",
    "    \"Deloitte\"\n",
    "]\n",
    "\n",
    "regions = [\n",
    "    \"North\",\n",
    "    \"South\",\n",
    "    \"East\",\n",
    "    \"West\"\n",
    "]\n",
    "\n",
    "products = {\n",
    "    \"Cloud Suite\": \"SaaS\",\n",
    "    \"Analytics Pro\": \"SaaS\",\n",
    "    \"Data Engine\": \"Platform\",\n",
    "    \"AI Insights\": \"AI\",\n",
    "    \"Security Shield\": \"Cybersecurity\",\n",
    "    \"Finance Tracker\": \"FinTech\",\n",
    "    \"HR Automator\": \"HRTech\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "92e60d7e-88ec-41b9-b112-323bccfeedaf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ==========================================\n",
    "# DATA GENERATION\n",
    "# ==========================================\n",
    "\n",
    "data = []\n",
    "\n",
    "for order_id in range(1001, 1501):\n",
    "\n",
    "    # Random product\n",
    "    product = random.choice(list(products.keys()))\n",
    "\n",
    "    # Category mapping\n",
    "    category = products[product]\n",
    "\n",
    "    # Quantity\n",
    "    quantity = random.randint(1, 5)\n",
    "\n",
    "    # Unit price\n",
    "    unit_price = random.randint(3000, 10000)\n",
    "\n",
    "    # Revenue calculation\n",
    "    revenue = quantity * unit_price\n",
    "\n",
    "    # Random date in 2025\n",
    "    order_date = fake.date_between(\n",
    "        start_date='-12M',\n",
    "        end_date='today'\n",
    "    )\n",
    "\n",
    "    # Append row\n",
    "    data.append({\n",
    "        \"order_id\": order_id,\n",
    "        \"order_date\": order_date,\n",
    "        \"customer_name\": random.choice(customers),\n",
    "        \"region\": random.choice(regions),\n",
    "        \"product\": product,\n",
    "        \"category\": category,\n",
    "        \"quantity\": quantity,\n",
    "        \"unit_price\": unit_price,\n",
    "        \"revenue\": revenue\n",
    "    })"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8001744b-90e0-4de0-8ba9-9ba7da43c2bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# ==========================================\n",
    "# CREATE DATAFRAME\n",
    "# ==========================================\n",
    "\n",
    "df = pd.DataFrame(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3254903d-0c8a-4fac-8e21-14a4ab0522cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sales_data.csv generated successfully!\n",
      "   order_id  order_date customer_name region          product       category  \\\n",
      "0      1001  2026-03-14           TCS   West    Analytics Pro           SaaS   \n",
      "1      1002  2025-06-14           IBM  North      Cloud Suite           SaaS   \n",
      "2      1003  2026-02-08     Capgemini  North    Analytics Pro           SaaS   \n",
      "3      1004  2026-01-06           HCL   East  Security Shield  Cybersecurity   \n",
      "4      1005  2025-12-03     Accenture  North      Data Engine       Platform   \n",
      "\n",
      "   quantity  unit_price  revenue  \n",
      "0         1        9554     9554  \n",
      "1         4        3894    15576  \n",
      "2         3        7517    22551  \n",
      "3         1        8089     8089  \n",
      "4         2        4812     9624  \n"
     ]
    }
   ],
   "source": [
    "# ==========================================\n",
    "# EXPORT CSV\n",
    "# ==========================================\n",
    "\n",
    "df.to_csv(\"sales_data.csv\", index=False)\n",
    "\n",
    "print(\"sales_data.csv generated successfully!\")\n",
    "print(df.head())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
