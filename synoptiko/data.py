# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pandas as pd
data_dir = os.path.dirname(__file__)

cancer_driver_genes_csv = os.path.join(data_dir, "cancer-driver-genes.csv")
cancer_driver_genes_df = pd.read_csv(cancer_driver_genes_csv)
cancer_driver_gene_id_set = set(cancer_driver_genes_df["Ensembl Gene ID"])

cancer_driver_variants_csv = os.path.join(data_dir, "cancer-driver-variants.csv")
cancer_driver_variants_df = pd.read_csv(cancer_driver_variants_csv)

class1_mhc_csv = os.path.join(data_dir, "class1-mhc-presentation-pathway.csv")
class1_mhc_df = pd.read_csv(class1_mhc_csv)
class1_mhc_gene_id_set = set(class1_mhc_df["Ensembl Gene ID"])

interferon_response_csv = os.path.join(data_dir, "interferon-response.csv")
interferon_response_df = pd.read_csv(interferon_response_csv)
interferon_response_gene_id_set = set(interferon_response_df["Ensembl Gene ID"])
