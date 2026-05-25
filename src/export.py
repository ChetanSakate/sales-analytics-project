# ==========================================
# EXPORT FUNCTIONS
# ==========================================

import os

def export_csv(df, output_path):
    """
    Export dataframe to CSV.
    """

    # Create folder if missing
    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    # Export CSV
    df.to_csv(output_path, index=False)

    print(f"CSV exported successfully: {output_path}")


def export_text(summary, output_path):
    """
    Export executive summary text file.
    """

    # Create folder if missing
    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    # Export text file
    with open(
    output_path,
    "w",
    encoding="utf-8"
) as file:
        file.write(summary)

    print(f"Text report exported successfully: {output_path}")