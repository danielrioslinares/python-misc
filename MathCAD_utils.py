#!/usr/bin/python

"""
MathCAD_utils
    @version : 0.1.1
    @author : Daniel Ríos Linares (c) 2019, hasbornasu@gmail.com
    @description : utils I used to convert SAPWin transfer functions to operate
        with MathCAD Prime 4.0

    @license : GPL-3.0
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.
        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.
        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import re


# SAPWin2MathCAD(sapwin_exp)
#
#     @argument <str sapwin_exp> : expression output from SAPWin
#
#    @returns <str mathcad_exp> : expression prepared to be copied to MathCAD
#        Prime 4.0
#
#     @description : convert SAPWin transfer functions to operate with MathCAD
#        Prime 4.0
#
#     @author : Daniel Ríos Linares
#
#    @version : 0.1.0
#
def SAPWin2MathCAD(sapwin_exp):

    # Prepare MathCAD output string for expression
    mathcad_exp = "" # <--------------------------------------------------------

    # Arguments of the function
    args = []

    # For both numerator and denominator
    for sapwin_pol in sapwin_exp.split("-" * 78):
        # Remove new line chars
        sapwin_pol = sapwin_pol.replace("\n","")
        # Get inside each s^(i) collection
        sapwin_pol_pars = [sapwin_pol_par.split(')')[0] for sapwin_pol_par in sapwin_pol.split('(') if sapwin_pol_par not in ("")]
        # Detect s^(i) for each i
        ss = []
        for s in [sapwin_pol_par.split(')')[1:][0] for sapwin_pol_par in sapwin_pol.split('(') if len(sapwin_pol_par.split(')')) != 1]:
            s2 = s.replace(" ","")
            print(s2)
            if s2 == "":
                ss.append(0)
            elif s2 == "s":
                ss.append(1)
            else:
                ss.append(int(s2[2:]))

        # Prepare MathCAD output string for polynomial
        mathcad_pol = "" # <----------------------------------------------------

        # For each s^(i) parentheses
        for i,sapwin_pol_par in zip(ss,sapwin_pol_pars[1:]):
            # Monomials are splitted (unsigned)
            sapwin_pol_par_mons = [sapwin_pol_par_mon for sapwin_pol_par_mon in re.split("([+-]+)", sapwin_pol_par) if sapwin_pol_par_mon not in ("", " ", "  ")]
            # Monomials are splitted (signed)
            sapwin_pol_par_mons = [sapwin_pol_par_mons[i]+sapwin_pol_par_mons[i+1] for i in range(0,len(sapwin_pol_par_mons),2)]
            # Prepare MathCAD output string for parentheses and polynomial
            mathcad_pol_par = "" # <--------------------------------------------

            # For each polynomial
            for sapwin_pol_par_mon in sapwin_pol_par_mons:
                # Split into variables
                sapwin_pol_par_mon_vars = sapwin_pol_par_mon.split(" ")
                # Prepare MathCAD output string for monomials
                mathcad_pol_par_mon = "" # <------------------------------------

                # For each monomial
                for sapwin_pol_par_mon_var in sapwin_pol_par_mon_vars:
                    # Empty string -> next
                    if not sapwin_pol_par_mon_var:
                        continue
                    # Sign -> next
                    if sapwin_pol_par_mon_var[0] in ("+", "-"):
                        nxt_sign = sapwin_pol_par_mon_var[0]
                        continue
                    # Split into variables
                    sapwin_pol_par_mon_var_id = sapwin_pol_par_mon_var[0]
                    sapwin_pol_par_mon_var_sub = sapwin_pol_par_mon_var[1:]
                    # Variable declaration
                    if sapwin_pol_par_mon_var_sub:
                        mathcad_pol_par_mon_var = "(@ID {} (@SUB {}))".format(sapwin_pol_par_mon_var_id, sapwin_pol_par_mon_var_sub)
                    else:
                        mathcad_pol_par_mon_var = "(@ID {})".format(sapwin_pol_par_mon_var_id)
                    # New variable?
                    if mathcad_pol_par_mon_var not in args:
                        args.append(mathcad_pol_par_mon_var)
                    # Sign treatment
                    if not mathcad_pol_par_mon:
                        if nxt_sign == "+":
                            mathcad_pol_par_mon = mathcad_pol_par_mon_var
                        elif nxt_sign == "-":
                            mathcad_pol_par_mon = "(@NEG {})".format(mathcad_pol_par_mon_var)
                    else:
                        mathcad_pol_par_mon = "({} {} {})".format(nxt_sign, mathcad_pol_par_mon, mathcad_pol_par_mon_var)
                    nxt_sign = "*"

                # Parentheses : s^(i) collect
                if not mathcad_pol_par:
                    mathcad_pol_par = mathcad_pol_par_mon
                else:
                    mathcad_pol_par = "(+ {} {})".format(mathcad_pol_par, mathcad_pol_par_mon)

            # Parentheses : s^(i) collect
            mathcad_pol_par = "(@PARENS {})".format(mathcad_pol_par)
            if i > 0: mathcad_pol_par = "(* {} (^ s {}))".format(mathcad_pol_par, i)
            if not mathcad_pol:
                mathcad_pol = mathcad_pol_par
            else:
                mathcad_pol = "(+ {} {})".format(mathcad_pol, mathcad_pol_par)

        # Finally
        if not mathcad_exp:
            mathcad_exp = mathcad_pol
        else:
            mathcad_exp = "(/ {} {})".format(mathcad_exp, mathcad_pol)

    # Arguments
    if len(args) > 1:
        mathcad_fnc_args = "(@LABEL VARIABLE s)"
        for arg in args: mathcad_fnc_args = "(@SEP {} (@LABEL VARIABLE {}))".format(mathcad_fnc_args, arg)
    else:
        mathcad_fnc_args = "(@LABEL VARIBLE s)"
    # Function
    mathcad_fnc = "(:= (@FUNCTION (@LABEL VARIABLE (@ID V (@SUB O))) (@ARGS {})) {})".format(mathcad_fnc_args, mathcad_exp)

    # Return it!
    return mathcad_fnc
################################################################################


# Example
if __name__ == "__main__":

    # Example output from SAPWin3
    example01 = """
    (  - VA R1 - VB R1 - VC R1)
    (  - VA RF2 RGB Rx Rx' + VB RF2 RGB Rx Rx') s^4
    ------------------------------------------------------------------------------
    (  - VA RF2 RGB Rx Rx' + VB RF2 RGB Rx Rx')
    """

    # Create mathcad_exp to be copied from the clipboard
    example01_mathcad_exp = SAPWin2MathCAD(example01)

    # We copy it from stdout
    print(example01_mathcad_exp)

    """ Expected output
    (:= (@FUNCTION (@LABEL VARIABLE (@ID V (@SUB O))) (@ARGS (@SEP (@SEP (@SEP (@LABEL VARIABLE s) (@LABEL VARIABLE (@ID V (@SUB A)))) (@LABEL VARIABLE (@ID R (@SUB 1)))) (@LABEL VARIABLE (@ID R (@SUB F2)))))) (/ (@PARENS (* (@NEG (@ID V (@SUB A))) (@ID R (@SUB 1)))) (@PARENS (* (@NEG (@ID V (@SUB A))) (@ID R (@SUB F2))))))
    """

    # Example output from SAPWin3
    example02 = """
    (  + V1 R50 + V1 R2)
    (  + V1 C1 R50 Rsig + V1 C1 R2 Rsig + V1 C1 R1 R50 + V1 C1 R1 R2 + V1 C2 R50 Rsig + V1 C2 R2 Rsig + V1 C2 R2 R50) s
    (  + V1 C2 C1 R2 R50 Rsig + V1 C2 C1 R1 R50 Rsig + V1 C2 C1 R1 R2 Rsig + V1 C2 C1 R1 R2 R50 + V1 C2 L1 R50 + V1 C2 L1 R2) s^2
    (  + V1 C2 C1 L1 R50 Rsig + V1 C2 C1 L1 R2 Rsig + V1 C2 C1 L1 R1 R50 + V1 C2 C1 L1 R1 R2) s^3
    ------------------------------------------------------------------------------
    (  + R50 Rsig + R2 Rsig)
    (  + C1 R1 R50 Rsig + C1 R1 R2 Rsig + C2 R2 R50 Rsig + L1 R50 + L1 R2) s
    (  + C2 C1 R1 R2 R50 Rsig + C1 L1 R50 Rsig + C1 L1 R2 Rsig + C1 L1 R1 R50 + C1 L1 R1 R2 + C2 L1 R2 R50) s^2
    (  + C2 C1 L1 R2 R50 Rsig + C2 C1 L1 R1 R2 R50) s^3
    """

    # Create mathcad_exp to be copied from the clipboard
    example02_mathcad_exp = SAPWin2MathCAD(example02)

    # We copy it from stdout
    print(example02_mathcad_exp)

    """ Expected output
    (:= (@FUNCTION (@LABEL VARIABLE (@ID V (@SUB O))) (@ARGS (@SEP (@SEP (@SEP (@LABEL VARIABLE s) (@LABEL VARIABLE (@ID V (@SUB A)))) (@LABEL VARIABLE (@ID R (@SUB 1)))) (@LABEL VARIABLE (@ID R (@SUB F2)))))) (/ (@PARENS (* (@NEG (@ID V (@SUB A))) (@ID R (@SUB 1)))) (@PARENS (* (@NEG (@ID V (@SUB A))) (@ID R (@SUB F2))))))
    """
#
