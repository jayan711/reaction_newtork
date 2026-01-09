from rdkit import Chem
from rdkit.Chem import AllChem

RULE = "[C+1:1].[I+0:2]>>[C+0:1]-[I+1;H0:2]"

rxn = AllChem.ReactionFromSmarts(RULE)

cation = Chem.MolFromSmiles("[C+1:1]")
anion = Chem.MolFromSmiles("[I:2]")

products = rxn.RunReactants((cation, anion))

for ps in products:
    for mol in ps:
        print(Chem.MolToSmiles(mol))


