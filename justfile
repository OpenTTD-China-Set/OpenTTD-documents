# Just isn't required to build the documentation
# all commands listed here can be run separately

# Default target
default: rm build

# remove _build directory
rm:
    @echo "Removing _build directory..."
    rm -rf _build

# Build the documentation
build:
    @echo "Building documentation..."
    sphinx-build -b html . _build
