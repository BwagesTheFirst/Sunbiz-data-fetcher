  #!/usr/bin/env python3
  """
  Fetch SunBiz data from Florida Department of State
  This script downloads corporate data and makes it available for WordPress
  """
  import os
  import json
  from datetime import datetime

  # Configuration
  DATA_DIR = "data"

  def download_sunbiz_data():
      """Download quarterly corporate data from SunBiz"""
      print(f"Starting SunBiz data fetch at {datetime.now()}")

      # Create data directory
      os.makedirs(DATA_DIR, exist_ok=True)

      # For now, create sample data to test the workflow
      create_sample_data()

      # Create a status file
      status = {
          "last_update": datetime.now().isoformat(),
          "status": "success",
          "message": "Sample data created successfully"
      }

      with open(os.path.join(DATA_DIR, "status.json"), "w") as f:
          json.dump(status, f, indent=2)

      print("Data fetch completed successfully")

  def create_sample_data():
      """Create sample data file for testing"""
      print("Creating sample HOA data...")

      # Create a sample fixed-width data file (1440 chars per line)
      associations = [
          ("M000000000001", "PELICAN BAY FOUNDATION INC", "NAPLES", "34108"),
          ("M000000000002", "FIDDLERS CREEK COMMUNITY ASSOCIATION INC", "NAPLES", "34114"),
          ("M000000000003", "BONITA BAY CLUB INC", "BONITA SPRINGS", "34134"),
          ("M000000000004", "THE BROOKS COMMUNITY ASSOCIATION INC", "BONITA SPRINGS", "34135"),
          ("M000000000005", "MIROMAR LAKES COMMUNITY ASSOCIATION INC", "ESTERO", "33913"),
      ]

      content = ""
      for doc_num, name, city, zip_code in associations:
          # Create fixed-width record (1440 characters)
          record = doc_num.ljust(12)  # Document number
          record += name.ljust(192)    # Entity name
          record += "A"                # Status (Active)
          record += "CONDO".ljust(15)  # Type

          # Add address fields
          record += "123 Main St".ljust(42)      # Address 1
          record += "".ljust(42)                  # Address 2
          record += city.ljust(28)                # City
          record += "FL".ljust(2)                 # State
          record += zip_code.ljust(10)            # Zip
          record += "US".ljust(2)                 # Country

          # Pad to 1440 characters
          record = record.ljust(1440)
          content += record + "\n"

      # Save to file
      output_file = os.path.join(DATA_DIR, "cordata0.txt")
      with open(output_file, "w") as f:
          f.write(content)

      print(f"Created {output_file} with {len(associations)} sample associations")

  if __name__ == "__main__":
      download_sunbiz_data()
