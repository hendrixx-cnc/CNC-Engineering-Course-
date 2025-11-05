import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import { remark } from 'remark';
import html from 'remark-html';

const modulesDirectory = path.resolve(process.cwd(), '../../Modules');

// This function is not used in the app router, but it is good practice to keep it for static generation
export function getAllModuleIds() {
  const fileNames = fs.readdirSync(modulesDirectory);

  return fileNames.map((fileName) => {
    return {
      params: {
        id: fileName.replace(/\.md$/, ''),
      },
    };
  });
}

export async function getModuleData(id: string) {
  const glob = require('glob');
  const files = glob.sync(path.join(modulesDirectory, `**/${id}.md`));
  if (files.length === 0) {
    return {
      title: 'Module not found',
      contentHtml: '<p>Module not found</p>',
    };
  }
  const fullPath = files[0];
  const fileContents = fs.readFileSync(fullPath, 'utf8');

  // Use gray-matter to parse the post metadata section
  const matterResult = matter(fileContents);

  // Use remark to convert markdown into HTML string
  const processedContent = await remark()
    .use(html)
    .process(matterResult.content);
  const contentHtml = processedContent.toString();

  // Combine the data with the id and contentHtml
  return {
    id,
    contentHtml,
    ...(matterResult.data as { title: string }),
  };
}
