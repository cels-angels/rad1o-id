# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.0

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build

# Utility rule file for rad1o_id_swig_swig_doc.

# Include the progress variables for this target.
include swig/CMakeFiles/rad1o_id_swig_swig_doc.dir/progress.make

swig/CMakeFiles/rad1o_id_swig_swig_doc: swig/rad1o_id_swig_doc.i

swig/rad1o_id_swig_doc.i: swig/rad1o_id_swig_doc_swig_docs/xml/index.xml
	$(CMAKE_COMMAND) -E cmake_progress_report /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating python docstrings for rad1o_id_swig_doc"
	cd /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/docs/doxygen && /usr/bin/python2 -B /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/docs/doxygen/swig_doc.py /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/swig/rad1o_id_swig_doc_swig_docs/xml /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/swig/rad1o_id_swig_doc.i

swig/rad1o_id_swig_doc_swig_docs/xml/index.xml: swig/_rad1o_id_swig_doc_tag
	$(CMAKE_COMMAND) -E cmake_progress_report /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating doxygen xml for rad1o_id_swig_doc docs"
	cd /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/swig && ./_rad1o_id_swig_doc_tag
	cd /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/swig && /usr/bin/doxygen /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/swig/rad1o_id_swig_doc_swig_docs/Doxyfile

rad1o_id_swig_swig_doc: swig/CMakeFiles/rad1o_id_swig_swig_doc
rad1o_id_swig_swig_doc: swig/rad1o_id_swig_doc.i
rad1o_id_swig_swig_doc: swig/rad1o_id_swig_doc_swig_docs/xml/index.xml
rad1o_id_swig_swig_doc: swig/CMakeFiles/rad1o_id_swig_swig_doc.dir/build.make
.PHONY : rad1o_id_swig_swig_doc

# Rule to build all files generated by this target.
swig/CMakeFiles/rad1o_id_swig_swig_doc.dir/build: rad1o_id_swig_swig_doc
.PHONY : swig/CMakeFiles/rad1o_id_swig_swig_doc.dir/build

swig/CMakeFiles/rad1o_id_swig_swig_doc.dir/clean:
	cd /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/rad1o_id_swig_swig_doc.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/rad1o_id_swig_swig_doc.dir/clean

swig/CMakeFiles/rad1o_id_swig_swig_doc.dir/depend:
	cd /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/swig /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/swig /home/jkraemer/Documents/src/rad1o-id/gr-rad1o_id/build/swig/CMakeFiles/rad1o_id_swig_swig_doc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/rad1o_id_swig_swig_doc.dir/depend
