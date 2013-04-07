import ply.yacc as yacc

def generate_parser(lexer, tokens):
  def p_empty(p):
    'empty :'
    pass
  
  def p_prod(p):
    'program : definition'
    '        | program definition'
    p[0] = p[1]

  def p_definition(p):
    'definition : trait_definition'
    p[0] = p[1]

  def p_trait_definition(p):
    'trait_definition : TRAIT trait_identifier INDENT description_string INDENT s_directive'
#    'trait_definition : TRAIT trait_identifier INDENT description_string INDENT s_directive INDENT f_directive'
    #TODO: Implement f_directive
    p[0] = (p[2], p[4], p[6], p[8])

  def p_trait_identifier(p):
    'trait_identifier : ID'
    p[0] = p[1]

  def p_description_string(p):
    'description_string : STRING_VAL'
    p[0] = p[1]

  def p_s_directive(p):
    's_directive : START COLON INDENT INDENT start_list'
    p[0] = p[5]

  def p_start_list(p):
    'start_list : statement_list'
    p[0] = p[1]

  def p_statement_list(p):
    'statement_list : compound_statement_list'
    '               | empty'
    p[0] = p[1]

  def p_compound_statement_list(p):
    'compound_statement_list : statement statement_list'
    p[0] = p[2] + [p[1]]

  def p_statement(p):
#    'statement : execute'
#    '          | print'
    'statement : print'
    '          | add'
    '          | remove'
    '          | move'
    '          | increase'
    '          | decrease'
    '          | initiate'
    '          | conditional'
    '          | using'
    p[0] = p[1]

#TODO: implement functions
#  def p_execute(p):
#    'execute : EXECUTE function_id optional_args'
#    p[0] = tuple(p[1:])
#
#  def p_function_id(p):
#    'function_id : ID'
#    p[0] = p[1]
#
#  def p_optional_args(p):
#    ''
#    p[0] = p[1]

  def p_print(p):
    'print : PRINT string_expression'
    p[0] = tuple(p[1:])

  def p_add(p):
    'add : ADD quantity object_identifier to_or_nothing'
    '    | ADD primitive to_or_nothing'
    p[0] = tuple(p[1:])

  def p_quantity(p):
    'quantity : arithmetic_expression'
    '         | empty'
    p[0] = p[1]

  def p_arithmetic_expression(p):
    'arithmetic_expression : INTEGER_VAL'
    #TODO: Finish arithmetic expressions
    p[0] = p[1]

  def p_object_identifier(p):
    'object_identifier : ID'
    p[0] = p[1]

  def p_to_or_nothing(p):
    'to_or_nothing : TO object_chain'
    '              | empty'
    if len(p) == 3:
      p[0] = p[2]
    elif len(p) == 2:
      p[0] = None

  def p_object_chain(p):
    'object_chain : object_identifier ON object_chain'
    '             | object_identifier'
    if len(p) == 4:
      p[0] = [p[1]] + p[3]
    elif len(p) == 2:
      p[0] = [p[1]]

  def p_primitive(p):
    'primitive : integer_primitive'
    #TODO: Add other primitives
    p[0] = p[1]

  def p_integer_primitive(p):
    'integer_primitive : LBRACE INTEGER ID EQUALS arithmetic_expression'
    p[0] = (p[2], p[3], p[5])

  def p_string_expression(p):
    'string_expression : STRING_VAL'
#    'string_expression : string_list'
#    '                  | object_expression'
#    '                  | STRING_VAL'
    #TODO: FIX strings
    p[0] = p[1]

  def p_remove(p):
    'remove : REMOVE quantity object_identifier from_or_nothing'
    '       | REMOVE primitive from_or_nothing'
    p[0] = tuple(p[1:])

  def p_from_or_nothing(p):
    'from_or_nothing : FROM object_chain'
    '              | empty'
    if len(p) == 3:
      p[0] = p[2]
    elif len(p) == 2:
      p[0] = None

  def p_move(p):
    'move : MOVE character_or_nothing TO object_chain'
    p[0] = p[2]

  def p_character_or_nothing(p):
    'character_or_nothing : character_identifier'
    '                     | empty'
    p[0] = p[1]

  def p_character_identifier(p):
    'character_identifier : ID'
    p[0] = p[1]

  def p_increase(p):
    'increase : INCREASE object_chain BY arithmetic_expression'
    p[0] = (p[1], p[2], p[4])

  def p_decrease(p):
    'decrease : DECREASE object_chain BY arithmetic_expression'
    p[0] = (p[1], p[2], p[4])

  def p_initiate(p):
    'initiate : INITIATE DIALOGUE AT label_identifier'
    p[0] = (p[1], p[4])

  def p_label_identifier(p):
    'label_identifier : LABEL'
    p[0] = p[1]

  def p_using(p):
    'using : USING STRING_VAL'
    p[0] = (p[1], p[2])



  def p_error(p):
    print "Syntax error in input!"

  return yacc.yacc()

