import os
import uncertainpy


folder = os.path.dirname(os.path.realpath(__file__))

test_data_dir = os.path.join(folder, "data")

seed = 10


def generate_data_allParameters(): # pragma: no cover
    parameterlist = [["a", 1, None],
                     ["b", 2, None]]

    parameters = uncertainpy.Parameters(parameterlist)
    model = uncertainpy.models.TestingModel1d(parameters)
    model.setAllDistributions(uncertainpy.Distribution(0.5).uniform)



    test = uncertainpy.UncertaintyEstimation(model,
                                             features=uncertainpy.TestingFeatures(),
                                             feature_list="all",
                                             output_dir_data=test_data_dir,
                                             output_dir_figures=test_data_dir,
                                             verbose_level="error",
                                             seed=seed)

    test.allParameters()

def generate_data_singleParameters():
    parameterlist = [["a", 1, None],
                     ["b", 2, None]]

    parameters = uncertainpy.Parameters(parameterlist)
    model = uncertainpy.models.TestingModel1d(parameters)
    model.setAllDistributions(uncertainpy.Distribution(0.5).uniform)



    test = uncertainpy.UncertaintyEstimation(model,
                                             features=uncertainpy.TestingFeatures(),
                                             feature_list="all",
                                             output_dir_data=test_data_dir,
                                             output_dir_figures=test_data_dir,
                                             verbose_level="error",
                                             seed=seed)


    test.singleParameters()


def generate_data_allParametersMC():
    parameterlist = [["a", 1, None],
                     ["b", 2, None]]

    parameters = uncertainpy.Parameters(parameterlist)
    model = uncertainpy.models.TestingModel1d(parameters)
    model.setAllDistributions(uncertainpy.Distribution(0.5).uniform)



    test = uncertainpy.UncertaintyEstimation(model,
                                             features=uncertainpy.TestingFeatures(),
                                             feature_list="all",
                                             output_dir_data=test_data_dir,
                                             output_dir_figures=test_data_dir,
                                             output_data_filename="TestingModel1d_MC",
                                             verbose_level="error",
                                             seed=seed,
                                             nr_mc_samples=10**1)

    test.allParametersMC()

def generate_data_singleParametersMC():
    parameterlist = [["a", 1, None],
                     ["b", 2, None]]

    parameters = uncertainpy.Parameters(parameterlist)
    model = uncertainpy.models.TestingModel1d(parameters)
    model.setAllDistributions(uncertainpy.Distribution(0.5).uniform)



    test = uncertainpy.UncertaintyEstimation(model,
                                             features=uncertainpy.TestingFeatures(),
                                             feature_list="all",
                                             output_dir_data=test_data_dir,
                                             output_dir_figures=test_data_dir,
                                             output_data_filename="TestingModel1d_MC",
                                             verbose_level="error",
                                             seed=seed,
                                             nr_mc_samples=10**1)


    test.singleParametersMC()



def generate_data_compareMC():
    parameterlist = [["a", 1, None],
                     ["b", 2, None]]

    parameters = uncertainpy.Parameters(parameterlist)
    model = uncertainpy.TestingModel1d(parameters)
    model.setAllDistributions(uncertainpy.Distribution(0.5).uniform)


    uncertainty = uncertainpy.UncertaintyEstimations(model,
                                                     features=uncertainpy.TestingFeatures(),
                                                     feature_list="all",
                                                     verbose_level="error",
                                                     output_dir_data=test_data_dir,
                                                     output_dir_figures=test_data_dir,
                                                     nr_mc_samples=10**1,
                                                     seed=seed)


    mc_samples = [10, 100]
    uncertainty.compareMC(mc_samples)



def generate_data_data():
    data = uncertainpy.Data()

    data.uncertain_parameters = ["a", "b"]
    data.feature_list = ["directComparison", "feature1"]
    data.t = {"feature1": [1., 2.], "directComparison": [3., 4.]}
    data.U = {"feature1": [1., 2.], "directComparison": [3., 4.]}
    data.E = {"feature1": [1., 2.], "directComparison": [3., 4.]}
    data.Var = {"feature1": [1., 2.], "directComparison": [3., 4.]}
    data.p_05 = {"feature1": [1., 2.], "directComparison": [3., 4.]}
    data.p_95 = {"feature1": [1., 2.], "directComparison": [3., 4.]}
    data.sensitivity = {"feature1": [1, 2], "directComparison": [3., 4.]}
    data.xlabel = "xlabel"
    data.ylabel = "ylabel"

    data.save(os.path.join(test_data_dir, "test_save_mock"))


if __name__ == "__main__":
    generate_data_allParameters()
    generate_data_singleParameters()
    generate_data_allParametersMC()
    generate_data_singleParametersMC()
    generate_data_compareMC()
    generate_data_data()
