import System.Random (randomRIO)

main :: IO ()
main = do
    first <- pick firstWord
    second <- pick secondWord
    putStr $ first ++ second ++ "\n"

{-generate :: []-}

pick :: [a] -> IO a
pick xs = randomRIO (0, (length xs - 1)) >>= return . (xs !!)

-------------------------------------------------------------------------------

firstWord = [
    -- Random words
    "LITTLE",
    "BANANA",
    "SPATULA",
    "SOUFFLE", -- NSA sure does like their souffle
    "HONEY",
    "PRESTON",
    "SECOND",
    "EGOTISTICAL",
    "MILD",
    "CACKLING",
    "SQUEAKY",
    "BACON",
    "CLEPTO",
    "STEAMY",

    -- Medical terms
    "HYPOXIC",
    "TUMOROUS",
    "NEURAL",
    "SANGUINE",
    "MELANCHOLIC",
    "CHOLERIC",
    "PHLEGMATIC",
    "BLEEDING",
    "HEART",
    "BRAIN",

    -- Business and politics
    "ROYAL",
    "STABLE",

    -- Tech
    "ONLINE",
    "WIRED"
    ]

-------------------------------------------------------------------------------

secondWord = [
    -- Random words
    "ORANGE",
    "GLEE",
    "CAPYBARA",
    "TROUGH",
    "SHAKE",
    "DEW",
    "MASS",
    "FROST",
    "PSYCHOSIS",
    "ABSCOND",
    "AGGRIEVE",
    "HATCHLING",
    "DOLPHIN",
    "BACON",
    "PARROT",
    "CARROT",
    "RIFT",
    "TIGER",
    "PIGEON",

    -- Medical terms
    "LESION",
    "JOINT",
    "ABSCESS",
    "CATARACT",
    "IRIS",
    "BLEED",

    -- Business and politics
    "SECRETARY",
    "AMENDMENT",
    "STATE"
    ]
