import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


churn = pd.read_csv('churn_final_data.csv',index_col=0)
bools = ['Techie', 'Churn', 'Port_modem', 'Tablet', 'Phone', 'Multiple', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'PaperlessBilling']
numerics = ['Lat','Lng','Population','Children','Age','Income','Outage_sec_perweek','Email','Contacts','Yearly_equip_failure','Tenure','MonthlyCharge','Bandwidth_GB_Year']
pcs = ['PC1','PC2','PC3','PC4','PC5','PC6','PC7','PC8','PC9','PC10','PC11','PC12','PC13','PC14','PC15','PC16','PC17','PC18','PC19','PC20','PC21','PC22','PC23','PC24','PC25','PC26']
churn = churn[numerics+bools]

churn_normalized=(churn-churn.mean())/churn.std()

pca = PCA(n_components=churn.shape[1])


pca.fit(churn_normalized)
churn_pca = pd.DataFrame(pca.transform(churn_normalized),columns=pcs)


plt.plot(pca.explained_variance_ratio_)
plt.xlabel('number of components')
plt.ylabel('explained variance')
plt.show()


cov_matrix = np.dot(churn_normalized.T, churn_normalized) / churn.shape[0]
eigenvalues = [np.dot(eigenvector.T, np.dot(cov_matrix, eigenvector)) for
eigenvector in pca.components_]

plt.plot(eigenvalues)
plt.xlabel('number of components')
plt.ylabel('eigenvalue')
plt.show() 



loadings = pd.DataFrame(pca.components_.T,
     columns=pcs,
     index=churn.columns)

print(loadings)
loadings.to_csv('pca_loadings.csv')