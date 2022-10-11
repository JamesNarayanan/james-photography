interface image {
	fullsize: string;
	thumb: string;
	description: string;
	location: string;
	exif: any;
}

type images = {
	[key: string]: image;
};

export { type images, type image };
