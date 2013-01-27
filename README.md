Most of the Haskell implementations are run in GHCI. This automatically makes it slower than by compiling using ghc and then running the executable.

In order to make to be able to run them in ghc, a main function needs to be created (main :: IO()) and compiled with the ghc command to create an executable
