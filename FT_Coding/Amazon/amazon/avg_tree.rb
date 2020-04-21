class ComponentNode
  attr_accessor :value, :components
  def initialize(value, components = [])
    @value = value
    @components = components
  end
end

class Tree
  attr_accessor :hash_map, :root

  def initialize
    @hash_map = {}
    @root = build_tree
  end

=begin
        200
      /     \
    120      180
    / | \    /  \
  110 20 20 150  80
=end

  def build_tree
    c1 = ComponentNode.new(110)
    c2 = ComponentNode.new(20)
    c3 = ComponentNode.new(20)
    c4 = ComponentNode.new(150)
    c5 = ComponentNode.new(80)
    c6 = ComponentNode.new(120, [c1, c2, c3])
    c7 = ComponentNode.new(180, [c4, c5])
    return(ComponentNode.new(200, [c6, c7]))
  end

  def find_average
    traverse_and_calculate(self.root)
    self.hash_map.max_by { |key, value| value }.first.value
  end

  def traverse_and_calculate(component)
    average = 0
    count = 0
    if component.components.empty?
      # self.hash_map[component] = component.value
      return [component.value, 1]
    end
    component.components.each do |child|
      avg, elements = traverse_and_calculate(child)
      average += (avg*elements + child.value)/(elements + 1)
      count += elements
      self.hash_map[child] = average
    end
    return [average, count]
  end
end

tree = Tree.new
puts(tree.find_average)
