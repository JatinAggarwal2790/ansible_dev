## In YAML, the > and | symbols (operators) are block scalar indicators used for writing multi-line strings, controlling how newlines are treated. 

# The > Operator (Folded Style) 
The > character indicates the folded style for multi-line strings. It treats newlines within the text as spaces, effectively joining the content into a single long line in the final output. 

## Behavior: Newlines are converted to spaces. Blank lines (double newlines in the source) are preserved as single newlines in the output. 
## Use Case: Ideal for long descriptions or paragraphs where the exact line breaks in the source file are not important for the final value. [1, 4, 7, 8, 9]  

Example: 
description: >
  This is a very long description
  that spans multiple lines in the YAML file
  but will be a single line in the output.

Resulting string: 
"This is a very long description that spans multiple lines in the YAML file but will be a single line in the output.\n" 

# The | Operator (Literal Style) 
The | character indicates the literal style. It preserves all newlines and original formatting exactly as they appear in the YAML file. 

## Behavior: Newlines are kept as literal newline characters () in the resulting string. 
## Use Case: Useful for formatted text, code snippets, or anything where whitespace and line breaks are significant. [4, 14, 15, 16, 17]  

Example: 
code: |
  line 1
  line 2
  line 3

Resulting string: "line 1\nline 2\nline 3\n"

# YAML supports several other options for defining data: 

## Unquoted Strings: Most strings do not require quotes unless they contain special characters (like :, #, [], {}, etc.) or reserved words (true, false, yes, no). 
## Single Quotes ('): Prevents most escape sequences from being processed, treating the content literally (except for ''  which becomes a single '). 
## Double Quotes ("): Allows C-style escape sequences (e.g., \n for a newline) to be interpreted. 
## Chomp Modifiers (-, +): These can be added to | or > to control how trailing newlines at the end of the block are handled: 

## |- or >- : Strips all trailing newlines. 
## |+ or >+ : Keeps all trailing newlines. 

### Lists (Sequences): Use a hyphen and a space (- ) for each item, or square brackets for inline flow style (e.g. [item1, item2] ). 
### Dictionaries (Mappings): Use key:value pairs, with indentation defining the hierarchy, or curly braces for inline flow style (e.g. {key1: value1, key2:value2}). 
### Anchors and Aliases: Use & to define an anchor and * to reference it later, which helps in avoiding data redundancy