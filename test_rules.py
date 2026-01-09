from rdkit import Chem
from rdkit.Chem import AllChem

MOLECULE = "C[Br+]"
RULE = "[C+0:1]-[Br+1:2]>>[C+1:1].[Br+0:2]"

mol = Chem.MolFromSmiles(MOLECULE)

rxn = AllChem.ReactionFromSmarts(RULE)
# mol = Chem.AddHs(mol)  # add for ones with H

products = rxn.RunReactants([mol])

for product in products:
    print(Chem.MolToCXSmiles(product[0]))
    print(Chem.MolToCXSmiles(product[1]))
