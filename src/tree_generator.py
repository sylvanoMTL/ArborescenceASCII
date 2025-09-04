import os
import toml
from datetime import datetime


class TreeGenerator:
	def __init__(self, toml_file_path="file_details.toml", max_filename_length=64):
		self.toml_file_path = toml_file_path
		self.max_filename_length = max_filename_length
		self.config = self.load_config()
		self.longest_display_name = 0
	
	def set_max_filename_length(self, length):
		"""Set maximum filename length"""
		self.max_filename_length = length
	
	def get_max_filename_length(self):
		"""Get current maximum filename length"""
		return self.max_filename_length
	
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
	
	def truncate_filename(self, filename):
		"""Truncate filename if it exceeds max length"""
		if len(filename) <= self.max_filename_length:
			return filename
		return filename[:self.max_filename_length-3] + "..."
	
	def calculate_longest_display_name(self, folder_path, prefix=""):
		"""Calculate the longest display name in the entire tree"""
		max_length = 0
		
		try:
			# Check root folder name
			folder_name = os.path.basename(folder_path) or folder_path
			truncated_name = self.truncate_filename(folder_name)
			max_length = max(max_length, len(truncated_name))
			
			# Check all items recursively
			all_items = sorted(os.listdir(folder_path))
			
			for item in all_items:
				item_path = os.path.join(folder_path, item)
				truncated_item = self.truncate_filename(item)
				
				# Calculate display length including tree symbols and prefix
				tree_symbols = "├── "  # Or "└── "
				display_length = len(prefix) + len(tree_symbols) + len(truncated_item)
				max_length = max(max_length, display_length)
				
				# If it's a directory, recursively check its contents
				if os.path.isdir(item_path):
					try:
						next_prefix = prefix + "│   "
						sub_max = self.calculate_longest_display_name(item_path, next_prefix)
						max_length = max(max_length, sub_max)
					except PermissionError:
						pass
		
		except PermissionError:
			pass
		
		return max_length
	
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
			headers.append("NAME")
		
		if self.config.get("common", {}).get("Type", False):
			headers.append("TYPE")
		
		if self.config.get("common", {}).get("Size", False):
			headers.append("SIZE")
		
		if self.config.get("common", {}).get("DateModified", False):
			headers.append("MODIFIED")
		
		if self.config.get("common", {}).get("DateCreated", False):
			headers.append("CREATED")
		
		if self.config.get("common", {}).get("DateAccessed", False):
			headers.append("ACCESSED")
		
		if len(headers) > 1:
			# Calculate spacing for filename column
			filename_width = max(self.longest_display_name + 2, len(headers[0]) + 2)
			
			# Format metadata headers with proper spacing
			metadata_headers = headers[1:]  # Exclude "NOM"
			column_widths = [12, 12, 20, 20, 20]
			formatted_headers = []
			
			for i, header in enumerate(metadata_headers):
				if i < len(column_widths):
					formatted_headers.append(header.ljust(column_widths[i]))
				else:
					formatted_headers.append(header)
			
			# Create header line with proper filename column width
			name_header = headers[0].ljust(filename_width)
			metadata_header_line = " ".join(formatted_headers).rstrip()
			header_line = name_header + metadata_header_line
			
			separator_line = "=" * len(header_line)
			sub_separator = "-" * len(header_line)
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
				
				# Truncate filename if too long
				truncated_item = self.truncate_filename(item)
				
				# Create the name part with tree structure
				name_part = f"{prefix}{current_prefix}{truncated_item}"
				
				# Get and format metadata
				metadata_parts = self.get_file_metadata(item_path, is_directory)
				
				if metadata_parts:
					formatted_metadata = self.format_metadata_line(metadata_parts)
					# Pad name part to align metadata
					padded_name = name_part.ljust(self.longest_display_name + 2)
					line = f"{padded_name}{formatted_metadata}"
				else:
					line = name_part
				
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
		
		# First pass: calculate the longest display name in the entire tree
		self.longest_display_name = self.calculate_longest_display_name(folder_path)
		
		# Generate header
		header = self.generate_header()
		
		# Generate root line
		folder_name = os.path.basename(folder_path) or folder_path
		truncated_folder_name = self.truncate_filename(folder_name)
		root_metadata_parts = self.get_file_metadata(folder_path, True)
		
		if root_metadata_parts:
			formatted_metadata = self.format_metadata_line(root_metadata_parts)
			# Pad root name to align with other entries
			padded_root = truncated_folder_name.ljust(self.longest_display_name + 2)
			root_line = f"{padded_root}{formatted_metadata}"
		else:
			root_line = truncated_folder_name
		
		# Generate tree content
		tree_lines = [root_line]
		tree_lines.extend(self.generate_tree_lines(folder_path))
		
		return header + "\n".join(tree_lines)


# Convenience function for simple usage
def generate_tree_structure(folder_path, toml_config_path="file_details.toml", max_filename_length=180):
	"""Simple function to generate tree structure"""
	generator = TreeGenerator(toml_config_path, max_filename_length)
	return generator.generate_tree(folder_path)