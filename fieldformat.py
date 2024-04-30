from dbfread import DBF

def field_formatter(filename):
# Open the DBF file
    with DBF(filename, ignorecase=True) as dbf:
        # Get field names and types
        fields = dbf.fields

        # Define a dictionary to map field types to their corresponding format
        type_mapping = {
            'C': 'C({})',  # Character
            'N': 'N({}, {})',  # Numeric
            'D': 'D',  # Date
            'L': 'L'  # Logical
        }

        # Format the fields according to the desired format
        formatted_fields = []
        for field in fields:
            field_type = type_mapping.get(field.type, field.type)
            if field.decimal_count is not None:
                formatted_field = f"{field.name} {field_type.format(field.length, field.decimal_count)}"
            else:
                formatted_field = f"{field.name} {field_type.format(field.length)}"
            formatted_fields.append(formatted_field)

        # Join the formatted fields into a single string
        formatted_fields_str = "; ".join(formatted_fields)

        # Print the formatted fields
        return(formatted_fields_str)