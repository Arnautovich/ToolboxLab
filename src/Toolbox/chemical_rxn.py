import rdkit
import numpy as np
import pubchempy as pcp
import pandas as pd
from rdkit.Chem import AllChem, Draw

class elements:
    def __init__(self, name:str)->None:
        '''
        This function initializes the class elements.The input parameters are:
        - name: str: the name of the element

        The function affects the following attributes:
        - name: str: the name of the element
        - properties: dict: a dictionary containing the properties of the element
        - smile: str: the SMILES representation of the element
        - mol: rdkit.Chem.Mol: the rdkit molecule object of the element
        - atoms_nb: dict: a dictionary containing the number of atoms of each type in the element

        The function raises a ValueError if the element is not found. If it is the case, try to use the english 
        name of the element.
        '''
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        
        try:
            compound = pcp.get_compounds(name, 'name')
            self.properties = pcp.get_properties(['canonical_smiles','MolecularWeight', 'XLogP', 'IUPACName', 'monoisotopic_mass', 'h_bond_acceptor_count', 'h_bond_donor_count'], name, 'name')[0]
            self.smile = compound[0].canonical_smiles
            self.mol = rdkit.Chem.MolFromSmiles(self.smile)
            self.name = name
            
        except:
            raise ValueError(f"Compound {name} not found")

        

        atoms = {}
        for atom in rdkit.Chem.AddHs(self.mol).GetAtoms():
            try:
                atoms[str(atom.GetSymbol())] +=1
            except:
                atoms[str(atom.GetSymbol())] = 1

        self.atoms_nb = atoms

    def draw(self):
        '''
        This function creates an image of the molecule. The function returns the image.
        '''
        return rdkit.Chem.Draw.MolToImage(self.mol)
    
    def add_stoichiometry(self, coef):
        '''
        This function adds the stoichiometry of the element to the properties dictionary. The input parameters are:
        - coef: float: the stoichiometry of the element
        '''

        up_dic = {'Stoichiometry': coef}
        self.properties = {**up_dic, **self.properties}


class equation:
    def __init__(self, rxn_str:str, op:list = ['->', '+']):
        '''
        This function initializes the class equation. The input parameters are:
        - rxn_str: the string representation of the chemical reaction
        - op:  a list of operators used to tokenize the reaction string

        The function affects the following attributes:
        - rxn_str: the string representation of the chemical reaction
        - rxn_tokenized: a list of tokens of the reaction string
        - rxn_obj: a list of objects representing the reaction
        - set_atoms: a set of atoms present in the reaction
        - stoich_coeff: an array containing the stoichiometry of the reaction
        '''
        if not isinstance(rxn_str, str):
            raise TypeError("rxn_str must be a string")
        
        self.rxn_tokenized = tokenize(rxn_str)

        self.rxn_obj = []
        self.set_atoms = set()

        for i in self.rxn_tokenized:
            if i in op:
                self.rxn_obj.append(i)

            else:
                element = elements(i)
                self.set_atoms.update(element.atoms_nb.keys())
                self.rxn_obj.append(element)

        self.stoich_coeff = self.get_stoichiometry(self.get_matrix(self.set_atoms, self.rxn_obj))
        
    def get_matrix(self, set_atoms:set, rxn:list)->np.ndarray:
        '''
        This function creates a matrix representation of the chemical reaction. Where each row represents an atom 
        and each column represents a molecule. The input parameters are:
        - set_atoms: a set of atoms present in the reaction
        - rxn: a list of objects representing the reaction

        The function returns a numpy array representing the matrix.
        '''

        index = rxn.index("->")

        matrix = []
        array_coeff = []

        for atom in set_atoms:
            for i in range(len(rxn)):
                try:
                    coefficient = rxn[i].atoms_nb[atom]

                    if i < index:
                        array_coeff.append(coefficient)
                        
                    else:
                        array_coeff.append(-coefficient)
                        
                except:
                    if rxn[i] != "+" and rxn[i] != "->":
                        array_coeff.append(0)

            
            matrix.append(array_coeff)
            array_coeff = []        
            
        return np.array(matrix)

    def get_stoichiometry(self, matrix:np.ndarray)->np.ndarray:
        '''
        This function calculates the stoichiometry of the reaction. The input parameters are:
        - matrix: a matrix representation of the chemical reaction

        The function returns a numpy array containing the stoichiometry of the reaction.
        '''
        b = np.zeros(matrix.shape[0])

        sto = gauss_elimination(matrix, b)

        index = self.rxn_obj.index("->")

        idx = 0

        for i in range(len(self.rxn_obj)):
            if self.rxn_obj[i] != "+" and self.rxn_obj[i] != "->":
                if i < index:
                    a = -1

                else:
                    a = 1

                self.rxn_obj[i].add_stoichiometry(a*sto[idx])
                idx += 1
        
        return sto

    def draw_reaction(self):
        '''
        This function creates an image of the reaction. The function returns the image.
        '''
        index = self.rxn_obj.index("->")
        reactants = [self.rxn_obj[i].smile for i in range(index) if self.rxn_obj[i] != "+"]
        products = [self.rxn_obj[i].smile for i in range(index + 1, len(self.rxn_obj)) if self.rxn_obj[i] != "+"]
        
        # Create a reaction object
        reaction = AllChem.ReactionFromSmarts('.'.join(reactants) + '>>' + '.'.join(products), useSmiles=True)
        
        # Create an image of the reaction
        reaction_image = Draw.ReactionToImage(reaction)
        
        return reaction_image
    
    def get_reaction_properties(self):
        '''
        This function creates a dataframe containing the properties of the reaction. The function returns 
        the dataframe containing the properties.
        '''
        index = self.rxn_obj.index("->")
        columns = ['Stoichiometry','MolecularWeight','IUPACName','CanonicalSMILES', 'MonoisotopicMass', 'HBondDonorCount', 'HBondAcceptorCount','XLogP']

        dataframe = pd.DataFrame([self.rxn_obj[0].properties], columns = columns)

        for i in range(1,len(self.rxn_obj)):
            if self.rxn_obj[i] != "+" and self.rxn_obj[i] != "->":                    
                dataframe = pd.concat([dataframe, pd.DataFrame([self.rxn_obj[i].properties], columns = columns)], ignore_index = True)
                
        return dataframe
    

def tokenize(expression:str, op_l:list = ["->", "+"])->list:
    '''
    This function tokenizes a chemical reaction expression. The input parameters are:
    - expression: the chemical reaction expression
    - op_l: a list of operators used to tokenize the expression

    The function returns a list of tokens.
    '''
    fragment_list = [expression]
    next_fragment_list = []
        
    
    op_l.sort(reverse=True, key = len)

    # Loop through each operator, splitting the expression into a list of tokens
    # based on that operator
    for operators in op_l:
        for fragment in fragment_list:

            # If the operator is in the fragment, split the fragment into a list of tokens
            # and append that list to next_fragment_list
            if operators in fragment and fragment not in op_l:
                f = fragment.split(operators)
                
                

                b = 1
                while b != len(f):
                    f.insert(b,operators)

                    b += 2

                next_fragment_list += f

            # Otherwise, append the fragment to next_fragment_list
            else:
                next_fragment_list.append(fragment)


        if len(next_fragment_list) != 0:
            fragment_list = next_fragment_list.copy()
        
        next_fragment_list = []

    # Remove whitespace from each token
    for i in range(len(fragment_list)):
        fragment_list[i] = fragment_list[i].strip()
    

    return fragment_list


def permute(array:np.ndarray)->np.ndarray:
    '''
    This function sorts the rows of a matrix in decreasing order of the maximum element in the column. The input
    parameters are:
    - array: a numpy array

    The function returns a numpy array.
    '''

    sorted_array = np.copy(array)
    array_temp = np.copy(array)

    line, column = array_temp.shape

    for i in range(column):
        maximum = np.max(np.absolute(array_temp[i:,i]))
        index = np.where(np.absolute(array_temp[i:,i]) == maximum)[0][0] + i

        sorted_array[i] = array_temp[index]
        sorted_array[index] = array_temp[i]

        array_temp = np.copy(sorted_array)

    return sorted_array


def gauss_elimination(Y:np.ndarray,x:np.ndarray)->np.ndarray:
    '''
    This function solves a system of linear equations using the Gauss elimination method. The input parameters are:
    - Y: the matrix of the system of linear equations
    - x: the right-hand side of the system of linear equations
    '''

    
    A = np.copy(Y).astype(float)
    b = np.copy(x).astype(float)


    while A.shape[0] < A.shape[1]:
        add = np.zeros(A.shape[1])
        A = np.vstack((A, add))
        b = np.append(b, 0)

    while A.shape[0] > A.shape[1]:
        add = np.zeros(A.shape[0])
        A = np.hstack((A, add.reshape(-1,1)))


    A = permute(A)

    for i in range(A.shape[0]):
        for j in range(i+1, A.shape[0]):
            if A[j,i] != 0:
                fact = -A[j,i]/A[i,i]

                for k in range(i, A.shape[0]):
                    A[j,k] += fact*A[i,k]

                b[j] += fact*b[i]
        A = permute(A)




    for i in range(A.shape[0]):
        if A[i,i] < 1e-10 and A[i,i] > -1e-10:
            A[i,i] = 1
            b[i] = 1




    for i in range(A.shape[0]-1, -1, -1):
        for j in range(i-1, -1, -1):
            if A[j,i] != 0:
                
                fact = -A[j,i]/A[i,i]
                
                A[j,i] += fact*A[i,i]
                
                b[j] += fact*b[i]


    for i in range(A.shape[0]):
        b[i] /= A[i,i]
        A[i,i] /= A[i,i]

    return b


if __name__ == "__main__":
    print(tokenize("NaOH + HCl -> NaCl + H2O"))
    print(tokenize("NaOH+ HCl -> NaCl +H2O"))
    
    #print(equation("NaCl+H2SO4->NaHSO4+HCl").get_reaction_properties())