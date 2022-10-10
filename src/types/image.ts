interface image {
	src: string;
	description: string;
	location: string;
}

type images = {
	[key: string]: image;
};

export default images;
