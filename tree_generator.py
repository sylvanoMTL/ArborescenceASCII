import os
import toml
from datetime import datetime


class TreeGenerator:
	def __init__(self, toml_file_path="file_details.toml"):
		self.toml_file_path = toml_file_path
		self.config = self.load_config()
	
	def load_config(self):
		"""Load TOML configuration for file details"""
		try:
			with open(self.toml_file_path, "r", encoding="utf-8") as f:
				return toml.load(f)
		except FileNotFoundError:
			return {
				"common": {"Name": True, "Size": True, "Type": True, "DateModified": True}
			}
	
	def reload_config(self):
		"""Reload configuration from TOML file"""
		self.config = self.load_config()
	
	def format_file_size(self, size_bytes):
		"""Convert bytes to human readable format"""
		if size_bytes == 0:
			return "0 B"
		
		units = ['B', 'KB', 'MB', 'GB']
		unit_index = 0
		size = float(size_bytes)
		
		while size >= 1024 and unit_index < len(units) - 1:
			size /= 1024
			unit_index += 1
		
		if unit_index == 0:
			return f"{int(size)} {units[unit_index]}"
		else:
			return f"{size:.1f} {units[unit_index]}"
	
	def format_date(self, timestamp):
		"""Format timestamp to dd/mm/yyyy hh:mm"""
		dt = datetime.fromtimestamp(timestamp)
		return dt.strftime("%d/%m/%Y %H:%M")
	
	def get_file_metadata(self, file_path, is_directory=False):
		"""Get file metadata based on TOML configuration"""
		metadata_parts = []
		
		try:
			stat = os.stat(file_path)
			
			# Add type indicator
			if self.config.get("common", {}).get("Type", False):
				if is_directory:
					metadata_parts.append("[DOSSIER]")
				else:
					metadata_parts.append("")
			
			# Add size
			if self.config.get("common", {}).get("Size", False):
				if is_directory:
					metadata_parts.append("")
				else:
					metadata_parts.append(self.format_file_size(stat.st_size))
			
			# Add modification date
			if self.config.get("common", {}).get("DateModified", False):
				metadata_parts.append(self.format_date(stat.st_mtime))
			
			# Add creation date
			if self.config.get("common", {}).get("DateCreated", False):
				metadata_parts.append(self.format_date(stat.st_ctime))
			
			# Add access date
			if self.config.get("common", {}).get("DateAccessed", False):
				metadata_parts.append(self.format_date(stat.st_atime))
		
		except (OSError, PermissionError):
			# Create empty placeholders for each enabled field
			if self.config.get("common", {}).get("Type", False):
				metadata_parts.append("")
			if self.config.get("common", {}).get("Size", False):
				metadata_parts.append("")
			if self.config.get("common", {}).get("DateModified", False):
				metadata_parts.append("")
			if self.config.get("common", {}).get("DateCreated", False):
				metadata_parts.append("")
			if self.config.get("common", {}).get("DateAccessed", False):
				metadata_parts.append("")
		
		return metadata_parts
	
	def format_metadata_line(self, metadata_parts):
		"""Format metadata parts with fixed-width columns"""
		if not metadata_parts:
			return ""
		
		# Column widths: TYPE, SIZE, DATE_MOD, DATE_CRE, DATE_ACC
		column_widths = [12, 12, 20, 20, 20]
		formatted_parts = []
		
		for i, part in enumerate(metadata_parts):
			if i < len(column_widths):
				formatted_part = part.ljust(column_widths[i])
				formatted_parts.append(formatted_part)
			else:
				formatted_parts.append(part)
		
		return " ".join(formatted_parts).rstrip()
	
	def generate_header(self):
		"""Generate header based on enabled options"""
		headers = []
		
		if self.config.get("common", {}).get("Name", True):
			headers.append("NOM")
		
		if self.config.get("common", {}).get("Type", False):
			headers.append("TYPE")
		
		if self.config.get("common", {}).get("Size", False):
			headers.append("TAILLE")
		
		if self.config.get("common", {}).get("DateModified", False):
			headers.append("DATE MODIFICATION")
		
		if self.config.get("common", {}).get("DateCreated", False):
			headers.append("DATE CREATION")
		
		if self.config.get("common", {}).get("DateAccessed", False):
			headers.append("DATE ACCES")
		
		if len(headers) > 1:
			# Format metadata headers with proper spacing
			metadata_headers = headers[1:]  # Exclude "NOM"
			column_widths = [12, 12, 20, 20, 20]
			formatted_headers = []
			
			for i, header in enumerate(metadata_headers):
				if i < len(column_widths):
					formatted_headers.append(header.ljust(column_widths[i]))
				else:
					formatted_headers.append(header)
			
			header_line = headers[0] + " " + " ".join(formatted_headers).rstrip()
			separator_line = "=" * 120
			sub_separator = "-" * 120
			return f"{separator_line}\n{header_line}\n{sub_separator}\n\n"
		
		return ""
	
	def generate_tree_lines(self, folder_path, prefix=""):
		"""Generate tree structure lines with metadata"""
		items = []
		
		try:
			all_items = sorted(os.listdir(folder_path))
			
			for i, item in enumerate(all_items):
				item_path = os.path.join(folder_path, item)
				is_last_item = i == len(all_items) - 1
				is_directory = os.path.isdir(item_path)
				
				# Tree symbols
				if is_last_item:
					current_prefix = "└── "
					next_prefix = prefix + "    "
				else:
					current_prefix = "├── "
					next_prefix = prefix + "│   "
				
				# Get and format metadata
				metadata_parts = self.get_file_metadata(item_path, is_directory)
				
				if metadata_parts:
					formatted_metadata = self.format_metadata_line(metadata_parts)
					line = f"{prefix}{current_prefix}{item} {formatted_metadata}"
				else:
					line = f"{prefix}{current_prefix}{item}"
				
				items.append(line)
				
				# Recursively process directories
				if is_directory:
					try:
						sub_items = self.generate_tree_lines(item_path, next_prefix)
						items.extend(sub_items)
					except PermissionError:
						items.append(f"{next_prefix}[Permission Denied]")
		
		except PermissionError:
			items.append(f"{prefix}[Permission Denied]")
		
		return items
	
	def generate_tree(self, folder_path):
		"""Generate complete tree structure with header and content"""
		self.reload_config()
		
		# Generate header
		header = self.generate_header()
		
		# Generate root line
		folder_name = os.path.basename(folder_path) or folder_path
		root_metadata_parts = self.get_file_metadata(folder_path, True)
		
		if root_metadata_parts:
			formatted_metadata = self.format_metadata_line(root_metadata_parts)
			root_line = f"{folder_name} {formatted_metadata}"
		else:
			root_line = folder_name
		
		# Generate tree content
		tree_lines = [root_line]
		tree_lines.extend(self.generate_tree_lines(folder_path))
		
		return header + "\n".join(tree_lines)


# Convenience function for simple usage
def generate_tree_structure(folder_path, toml_config_path="file_details.toml"):
	"""Simple function to generate tree structure"""
	generator = TreeGenerator(toml_config_path)
	return generator.generate_tree(folder_path)