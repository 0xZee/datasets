import pandas as pd
from llama_index.core import Document
from llama_index.core.schema import NodeWithScore
from llama_index.core.schema import TextNode

def csv_to_nodes(csv_path):
    """
    Read a CSV file and convert each row to a Node in llama-index structure.
    
    Args:
        csv_path (str): Path to the CSV file
    
    Returns:
        list[TextNode]: List of TextNodes created from CSV rows
    """
  
    df = pd.read_csv(csv_path)
    
    # List to store nodes
    nodes = []

    # Convert rows of the CSV into Document objects
    #documents = [Document(text=row.to_string()) for _, row in df.iterrows()]
    
    # Iterate through each row
    for _, row in df.iterrows():
        text_lines = []
        for column, value in row.items():
            text_lines.append(f"{column} :\t{value}")
        
        text = "\n".join(text_lines)
        
        # Create metadata dictionary
        metadata = {
            'ticker': row.get('Symbol', ''),
            'market_cap': row.get('Market Cap', ''),
            'name': row.get('Company Name', '')
        }
        
        # Create a TextNode
        node = TextNode(
            text=text,
            metadata=metadata
        )
        
        nodes.append(node)
    
    return nodes

# Example usage
# nodes = csv_to_nodes('stocks.csv')
