// Compile with gcc blur.c $(pkg-config --cflags --libs imlib2) -o blur

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Imlib2.h>

#define NAME "imlib2_blur"

char **args;
int ignore_aspect = 0;

double max(double a, double b) {
	return a > b ? a : b;
}

void parse_options(int argc, char **argv, int argn) {
	if (argc <= 0) {
		if (argn != 5) {
			printf("Usage: \"" NAME " [-i] BLUR_RADIUS WIDTH HEIGHT SOURCE DEST\"\n");
			exit(1);
		}
	} else {
		if (strcmp(argv[0], "-i") == 0) {
			ignore_aspect = 1;
		} else {
			args[argn++] = argv[0];
		}
		argc--;
		argv++;

		return parse_options(argc, argv, argn);
	}
}

int main(int argc, char **argv) {
	// parse args
	args = malloc(5 * sizeof(char *));
	parse_options(--argc, ++argv, 0);

	// args to vars
	int radius = atoi(args[0]);
	int width = atoi(args[1]);
	int height = atoi(args[2]);
	char* source = args[3];
	char* dest = args[4];


	// get source image
	Imlib_Image src_image = imlib_load_image(source);
	// exit on fail
	if (!src_image)
		exit(2);

	// get width, height from source img
	imlib_context_set_image(src_image);
	int w = imlib_image_get_width();
	int h = imlib_image_get_height();
	int new_w, new_h;
	int offset_w, offset_h;

	if (!ignore_aspect) {
		// calc aspect
		double aspect_w = width / (double) w;
		double aspect_h = height / (double) h;
		aspect_h = max(aspect_w, aspect_h);
		aspect_w = max(aspect_w, aspect_h);

		new_w = width / aspect_w;
		new_h = height / aspect_h;
		offset_w = (w - new_w) / 2;
		offset_h = (h - new_h) / 2;
	} else {
		// offset_h = 0;
		// offset_w = 0;
		// new_w = w;
		// new_h = w;
	}

	// new blank image
	Imlib_Image dest_img = imlib_create_image(width, height);

	imlib_context_set_image(dest_img);
	imlib_blend_image_onto_image(src_image, 0, offset_w, offset_h, new_w, new_h, 0, 0, width, height);
	imlib_image_blur(radius);
	imlib_save_image(dest);
}